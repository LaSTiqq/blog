const arrow = document.getElementById("arrow");

if (arrow) {
	arrow.style.display = "none";
}

window.onscroll = function () {
	scrollFunction();
};

function scrollFunction() {
if (arrow) {
	if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
			// End value
			arrow.style.display = "block";
		} else {
			// Start value
			arrow.style.display = "none";
		}
	}
}