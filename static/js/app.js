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
        bubble.innerHTML = DOMPurify.sanitize(marked.parse(message));
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

            add_message("user", reply);

            const formData = new FormData(form);
            input.value = "";

            const response = await fetch(
                form.action || window.location.href,
                {
                    method: "POST",
                    body: formData,
                }
            );

            const reader = response.body.getReader();
            const decoder = new TextDecoder();

            let aiText = "";

            const aiBubble = add_message("ai", "");

            while (true) {
                const { value, done } = await reader.read();

                if (done) break;

                aiText += decoder.decode(value, { stream: true });

                aiBubble.innerHTML = DOMPurify.sanitize(
                    marked.parse(aiText)
                );

                messages.scrollTop = messages.scrollHeight;
            }

            aiText += decoder.decode();

            aiBubble.innerHTML = DOMPurify.sanitize(
                marked.parse(aiText)
            );

            const codeBlocks = aiBubble.querySelectorAll(
                'pre code[class^="language-"]'
            );

            codeBlocks.forEach((block) => {
                hljs.highlightElement(block);
            });


        }
    });
}