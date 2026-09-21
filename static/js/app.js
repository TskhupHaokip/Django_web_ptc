const input = document.getElementById("chatInput");
const form = document.getElementById("chat-form");
const messages = document.querySelector(".bubbles");

const add_message = (sender, message) => {
    const bubble = document.createElement("div");

    if (sender === "user") {
        bubble.classList.add("user", "p-4", "align-self-end");
        bubble.textContent = message;
    } else {
        bubble.classList.add("ai", "p-4", "align-self-start");
        bubble.innerHTML = DOMPurify.sanitize(
            marked.parse(message)
        );
    }

    messages.appendChild(bubble);

    return bubble;
};


if (input) {
    input.addEventListener("keydown", async (event) => {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault();

            const reply = input.value.trim();

            if (!reply) return;

            // Add user message
            add_message("user", reply);

            // Prepare form data before clearing input
            const formData = new FormData(form);
            input.value = "";

            // Send message to Django
            const response = await fetch(
                form.action || window.location.href,
                {
                    method: "POST",
                    body: formData,
                }
            );

            // Read streaming response
            const reader = response.body.getReader();
            const decoder = new TextDecoder();

            let aiText = "";

            // Create one AI bubble
            const aiBubble = add_message("ai", "");

            // Stream Gemini response
            while (true) {
                const { value, done } = await reader.read();

                if (done) break;

                aiText += decoder.decode(value, {
                    stream: true
                });

                // Render Markdown while streaming
                aiBubble.innerHTML = DOMPurify.sanitize(
                    marked.parse(aiText)
                );

                // Keep chat scrolled to bottom
                messages.scrollTop = messages.scrollHeight;
            }

            // Decode anything remaining in the decoder
            aiText += decoder.decode();

            // Final Markdown render
            aiBubble.innerHTML = DOMPurify.sanitize(
                marked.parse(aiText)
            );

            // Find code blocks
            const highlightedBlocks = aiBubble.querySelectorAll(
                'pre code[class^="language-"]'
            );

            // Syntax highlighting
            highlightedBlocks.forEach((block) => {
                hljs.highlightElement(block);
            });

            // Add headers + copy buttons
            const preBlocks = aiBubble.querySelectorAll("pre");

            preBlocks.forEach((pre) => {
                const code = pre.querySelector("code");

                if (!code) return;

                // Wrapper
                const wrapper = document.createElement("div");
                wrapper.classList.add("code-block");

                // Header
                const header = document.createElement("div");
                header.classList.add("code-header");

                // Language
                const language = document.createElement("span");

                language.textContent =
                    code.className.match(/language-(\w+)/)?.[1] || "code";

                // Copy button
                const copyButton = document.createElement("button");
                copyButton.type = "button";
                copyButton.classList.add("copy-btn");
                copyButton.innerHTML = '<i class="bi bi-copy"></i>';

                copyButton.addEventListener("click", async () => {
                    await navigator.clipboard.writeText(
                        code.textContent
                    );

                    copyButton.innerHTML =
                        '<i class="bi bi-check2"></i>';

                    setTimeout(() => {
                        copyButton.innerHTML =
                            '<i class="bi bi-copy"></i>';
                    }, 1500);
                });

                // Put language + button in header
                header.append(language, copyButton);

                // Replace <pre> with wrapper
                pre.parentNode.insertBefore(wrapper, pre);

                // Put header + code block inside wrapper
                wrapper.append(header, pre);
            });

            // Make sure we're at the bottom after rendering
            messages.scrollTop = messages.scrollHeight;
        }
    });
}