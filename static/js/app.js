const search = document.querySelector(".search-box")
const favButtons = document.querySelectorAll(".favourite-btn");

if (favButtons) {
    favButtons.forEach((button) => {
        const movieId = button.dataset.movieId;
        const title = button.dataset.title;

        button.addEventListener("click", () => {
            button.textContent = button.textContent === "🩷" ? "♡" : "🩷";

        });
    });
}


let timer;

if (search) {
    search.addEventListener("input", (event) => {
        const value = event.target.value.trim();

        clearTimeout(timer);

        if (!value) {
            return;
        }

        timer = setTimeout(() => {
            search.submit();
        }, 500);
    });
}
