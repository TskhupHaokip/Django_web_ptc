const toggle = document.getElementById("toggle")
const sidebar = document.querySelector(".sidebar")
const toast = document.getElementById("toast");
const message = document.getElementById("toast-message");
const sub_card = document.querySelector(".subscription-card");
const countdown = document.getElementById("countdown");
const plans = document.querySelectorAll(".plan-card");
const profileCard = document.querySelector(".profile-card");

const links ="plans/free"

const Plans_link = {
    free: "plans/free",
    pro: "plans/pro",
    business: "plans/business"
};

plans.forEach(plan => {
    plan.addEventListener("click", () => {

        const name = plan
            .querySelector(".plan-name")
            .textContent
            .trim()
            .toLowerCase();

        window.location.href = Plans_link[name];

        console.log(`${name} Clicked`);
    });
});



if (countdown) {
    const expiresAt = new Date(countdown.dataset.expires);

    function updateCountdown() {
        const now = new Date();
        const difference = expiresAt - now;

        if (difference <= 0) {
            countdown.textContent = "Expired";
            clearInterval(timer);
            return;
        }

        const totalSeconds = Math.floor(difference / 1000);

        const hours = Math.floor(totalSeconds / 3600);
        const minutes = Math.floor((totalSeconds % 3600) / 60);
        const seconds = totalSeconds % 60;

        countdown.textContent =
            `Expires in: ${hours}h ${minutes}m ${seconds}s`;
    }

    const timer = setInterval(updateCountdown, 1000);
    updateCountdown();

    
}


if (profileCard) {
    profileCard.addEventListener("click",() =>{
        window.location.href = "/users/profile";
    });
}

if (sub_card) {
    sub_card.addEventListener("click",() =>{
        window.location.href = "/subscription";
    });
}


function showToast(text) {
    message.textContent = text;
    toast.classList.add("show");

    setTimeout(() => {
        toast.classList.remove("show");
    }, 3000);
}

if (toggle) {
    toggle.addEventListener("click",() => {
    if (sidebar) {
        sidebar?.classList.toggle("show");
    }

    });
}