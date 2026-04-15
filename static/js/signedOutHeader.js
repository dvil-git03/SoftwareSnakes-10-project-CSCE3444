/*
    This function is similar to header_init.js, but the main difference is this
    is for logged out sessions. At the moment, there is no login app setup in Django,
    so it will just redirect to the "root" of this app, which is the home page.
*/

function setHeader(nameplate) {
    const element = document.getElementById("insert_header");

    element.innerHTML = `
    <div id="main-header" class="header">
        <div class="header-left">
            <div class="header-logo">
                    <a href="/">
                        <img class="main-logo" src="/static/images/logo.png" alt="Logo">
                    </a>
            </div>
        </div>
        <div class="header-center">
            <h1>${nameplate}</h1>
        </div>
        <div class="header-right">
            <div class="header-logo"><a href="/"><img src="/static/images/house_icon.png" alt="Logo"></a></div>
            <div class="header-logo"><a href="/"><img src="/static/images/globe_icon.png" alt="Logo"></a></div>
            <div class="header-logo"><a href="/"><img src="/static/images/smily_face.png" alt="Logo"></a></div>
            <div class="header-logo"><a href="/"><img src="/static/images/person_icon.png" alt="Logo"></a></div>
        </div>
    </div>
    `
}