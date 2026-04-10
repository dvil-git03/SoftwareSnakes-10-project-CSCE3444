const pencilButton = document.getElementById("pencilButton");
const expandingBox = document.getElementById("expandingBox");

//we gotta open this got darn box. but hooooow?!?!?
pencilButton.addEventListener("click", () => { //this part was 
// copilot ^
    expandingBox.classList.remove("hidden");
});

//we also gotta close the box. but how?!?!?
window.closeDown = function() {
    expandingBox.classList.add("hidden"); //gotta use hidden
    //as much as possible
}
