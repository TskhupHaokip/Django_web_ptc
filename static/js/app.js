const input = document.getElementById("chatInput");
const form = document.getElementById("chat-form");
const messages = document.querySelector(".bubbles");

const add_message = (sender, message) => {
    const bubble = document.createElement("div");
    bubble.textContent = message;

    if (sender === "user") {
        bubble.classList.add("user", "p-3", "align-self-end");
    } else {
        bubble.classList.add("ai", "p-3", "align-self-start");
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

            const aiBubble = add_message("ai", "");
            
            while (true) {
                const { value, done } = await reader.read();
                if (done) break;
                const chunk = decoder.decode(value, { stream: true });
                aiBubble.textContent += chunk;
                messages.scrollTop = messages.scrollHeight;
                
            }
        }
    });
}