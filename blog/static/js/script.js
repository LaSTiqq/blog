document.getElementById("arrow").style.display = "none";

window.onscroll = function () {
	scrollFunction();
};

function scrollFunction() {
if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
		// End value
		document.getElementById("arrow").style.display = "block";
	} else {
		// Start value
		document.getElementById("arrow").style.display = "none";
	}
}