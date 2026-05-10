document.getElementById("settings-btn").addEventListener("click", () =>{
    window.location.href = "/settings/";
});

const dateEl = document.getElementById("clock-date");
const timeEl = document.getElementById("clock-time");

function updateClock() {
    const now = new Date();

    const yyyy = now.getFullYear();
    const mo = String(now.getMonth() + 1).padStart(2,"0");
    const dd = String(now.getDate()).padStart(2,"0");
    dateEl.textContent = `${yyyy}/${mo}/${dd}`;

    const hh = String(now.getHours()).padStart(2,"0");
    const mm = String(now.getMinutes()).padStart(2,"0");
    const ss = String(now.getSeconds()).padStart(2,"0");
    timeEl.textContent  = `${hh}:${mm}:${ss}`;
}

updateClock();
setInterval(updateClock, 1000);