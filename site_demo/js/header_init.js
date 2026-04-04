function set_header(nameplate){
    const element = document.getElementById("insert_header");

    element.innerHTML = `
    <div id="main_header" class="header">
        <div class="header_left">
            <div class="header_logo">
                <a href="homepage.html"><img src="images/logo.png" alt="Logo"></a>
            </div>
        </div>
        <div class="header_center">
            <h1>${nameplate}</h1>
        </div>
        <div class="header_right">
            <div class="header_logo"><a href="myroom.html"><img src="images/house_icon.png" alt="Logo"></a></div>
            <div class="header_logo"><a href="explore.html"><img src="images/globe_icon.png" alt="Logo"></a></div>
            <div class="header_logo"><a href="friends.html"><img src="images/smily_face.png" alt="Logo"></a></div>
            <div class="header_logo"><a href="profile.html"><img src="images/person_icon.png" alt="Logo"></a></div>
        </div>
    </div>
    `
}