window.onscroll = function () {
  scrollFunction();
};

const arrow = document.getElementById("arrow");

function scrollFunction() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    // End value
    arrow.style.display = "block";
  } else {
    // Start value
    arrow.style.display = "none";
  }
}

[...document.querySelectorAll('[data-bs-toggle="tooltip"]')]
.forEach(el => new bootstrap.Tooltip(el))

hljs.initHighlightingOnLoad();