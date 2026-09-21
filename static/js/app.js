// const input = document.getElementById("chatInput");
// const form = document.getElementById("chat-form");
// const messages = document.querySelector(".bubbles");

// const add_message = (sender, message) => {
//     const bubble = document.createElement("div");

//     bubble.textContent = message;

//     if (sender === "user") {
//         bubble.classList.add("user", "p-2", "align-self-end");
//     } else {
//         bubble.classList.add("ai", "p-2", "align-self-start");
//     }

//     messages.appendChild(bubble);
// };

// const input = document.getElementById("chatInput");
// const form = document.getElementById("chat-form");
// const messages = document.querySelector(".bubbles");

// const add_message = (sender, message) => {
//     const bubble = document.createElement("div");
//     bubble.textContent = message;

//     if (sender === "user") {
//         bubble.classList.add("user", "p-2", "align-self-end");
//     } else {
//         bubble.classList.add("ai", "p-2", "align-self-start");
//     }

//     messages.appendChild(bubble);
// };

// if (input) {
//     input.addEventListener("keydown", (event) => {
//         if (event.key === "Enter" && !event.shiftKey) {
//             event.preventDefault();

//             const reply = input.value.trim();

//             if (!reply) return;
//             add_message("user",reply)
//             add_message("ai","idk")
//             // form.requestSubmit();

//         }
//     });
// }


// if (form) {

//     form.addEventListener("submit", async (event) => {
//         event.preventDefault();
//         const reply = input.value.trim();
//         if (!reply) return;
//         add_message("user", reply);
//         input.value = "";
//         const response = await fetch(form.action || window.location.href, {
//             method: "POST",
//             body: new FormData(form),
//         });

//         const data = await response.json();

//         add_message("ai", data.message);
//     });

// }

const input = document.getElementById("chatInput");
const form = document.getElementById("chat-form");
const messages = document.querySelector(".bubbles");

const add_message = (sender, message) => {
    const bubble = document.createElement("div");
    bubble.textContent = message;
    if (sender === "user") {
        bubble.classList.add("user", "p-2", "align-self-end");
    } else {
        bubble.classList.add("ai", "p-2", "align-self-start");
    }
    messages.appendChild(bubble);
};



if (input) {
    input.addEventListener("keydown", (event) => {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault();

            const reply = input.value.trim();

            if (!reply) return;

            add_message("user", reply);

            const formData = new FormData(form);
            input.value = "";

            fetch(form.action || window.location.href, {
                method: "POST",
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    add_message("ai", data.message);
                });
        }
    });
}