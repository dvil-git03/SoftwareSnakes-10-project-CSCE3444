/*
    This function creates the main websites header, by inserting a HTML element using DOM.
    Any changes to the header's markup need to be conducted here.
    This is done to reduce copying and pasting this element for each page of the website.
*/

function setHeader(nameplate) {
    const element = document.getElementById("insert_header");

    element.innerHTML = `
    <div id="main-header" class="header">
        <div class="header-left">
            <div class="header-logo">
                    <a href="home.html">
                        <img class="main-logo" src="images/logo.png" alt="Logo">
                    </a>
            </div>
        </div>
        <div class="header-center">
            <h1>${nameplate}</h1>
        </div>
        <div class="header-right">
            <div class="header-logo"><a href="myroom.html"><img src="images/house_icon.png" alt="Logo"></a></div>
            <div class="header-logo"><a href="explore.html"><img src="images/globe_icon.png" alt="Logo"></a></div>
            <div class="header-logo"><a href="friends.html"><img src="images/smily_face.png" alt="Logo"></a></div>
            <div class="header-logo"><a href="profile.html"><img src="images/person_icon.png" alt="Logo"></a></div>
        </div>
    </div>
    `
}