const currentTheme = localStorage.getItem("theme") || "light";
const toggleInput = document.querySelector("#toggle-mode");
const body = document.querySelector("body");

if (currentTheme === "dark") {
  body.classList.add("dark-mode");
  toggleInput.setAttribute("checked", true);
}

toggleInput.addEventListener("change", () => {
  body.classList.toggle("dark-mode");
  if (body.classList.contains("dark-mode")) {
    localStorage.setItem("theme", "dark");
  } else {
    localStorage.setItem("theme", "light");
  }
});

// Tooltip
document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach((el) => {
  new bootstrap.Tooltip(el);
});

// Code template
hljs.highlightAll();
