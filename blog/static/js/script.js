[...document.querySelectorAll('[data-bs-toggle="tooltip"]')].forEach(
  (el) => new bootstrap.Tooltip(el)
);

hljs.initHighlightingOnLoad();

const currentTheme = localStorage.getItem("theme");
const body = document.querySelector("body");
const toggle = document.getElementById("toggle");

if (currentTheme == "light") {
  body.classList.add("active");
}

toggle.addEventListener("click", function () {
  toggle.classList.toggle("active");
  body.classList.toggle("active");

  let theme = "dark";
  if (body.classList.contains("active")) {
    theme = "light";
  }
  localStorage.setItem("theme", theme);
});