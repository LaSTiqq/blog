//  Dark/Light mode
const currentTheme = localStorage.getItem("data-bs-theme");
const toggleInput = document.querySelector("#toggle-mode");
const html = document.querySelector("html");

if (currentTheme === "dark") {
  html.setAttribute("data-bs-theme", "dark");
  toggleInput.setAttribute("checked", true);
} else {
  html.setAttribute("data-bs-theme", "light");
}

toggleInput.addEventListener("change", () => {
  if (html.getAttribute("data-bs-theme") === "dark") {
    html.setAttribute("data-bs-theme", "light");
    localStorage.setItem("data-bs-theme", "light");
  } else {
    html.setAttribute("data-bs-theme", "dark");
    localStorage.setItem("data-bs-theme", "dark");
  }
});

// Tooltip
document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach((el) => {
  new bootstrap.Tooltip(el);
});

// Code highlight
Prism.highlightAll();

// AOS
AOS.init({
  disable: window.innerWidth < 1360,
  startEvent: "DOMContentLoaded",
  once: true,
});
