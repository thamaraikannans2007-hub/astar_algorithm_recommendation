function toggleTheme() {
    const body = document.body;
    body.classList.toggle("light-mode");
}
function showLoader() {
    document.getElementById("loader").classList.remove("hidden");
}
const toggle = document.getElementById("themeToggle");

if (localStorage.getItem("theme") === "light") {
    document.body.classList.add("light-mode");
    toggle.checked = true;
}

toggle.addEventListener("change", () => {
    document.body.classList.toggle("light-mode");

    if (toggle.checked) {
        localStorage.setItem("theme", "light");
    } else {
        localStorage.setItem("theme", "dark");
    }
});