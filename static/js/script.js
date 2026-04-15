// This function at the moment, is temporary, and needs further work.

const pencilButton = document.getElementById("pencilButton");
const expandingBox = document.getElementById("expandingBox");


pencilButton.addEventListener("click", () => {
    expandingBox.classList.remove("hidden");
});

window.closeDown = function () {
    expandingBox.classList.add("hidden");
}
