document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("theme-toggle");
    const rootElement = document.documentElement;
    const navbarBrand = document.getElementById("navbar-brand");
    const storedTheme = localStorage.getItem("theme");

    function updateTheme(theme) {
        rootElement.setAttribute("data-bs-theme", theme);
        localStorage.setItem("theme", theme);

        // Update button text and class
        if (theme === "dark") {
            themeToggle.innerHTML = "🌞";
            themeToggle.classList.remove("btn-light");
            themeToggle.classList.add("btn-outline-light");
            navbarBrand.classList.remove("navbar-brand-light"); // Dark mode: keep white
        } else {
            themeToggle.innerHTML = "🌙";
            themeToggle.classList.remove("btn-outline-light");
            themeToggle.classList.add("btn-light");
            navbarBrand.classList.add("navbar-brand-light"); // Light mode: dark text
        }
    }

    // Set initial theme
    if (storedTheme) {
        updateTheme(storedTheme);
    }

    themeToggle.addEventListener("click", function () {
        const newTheme = rootElement.getAttribute("data-bs-theme") === "dark" ? "light" : "dark";
        updateTheme(newTheme);
    });
});
document.getElementById('year').textContent = new Date().getFullYear();