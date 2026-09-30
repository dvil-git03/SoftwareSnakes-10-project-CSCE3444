/*
    profileModal.js
    The logic to handle profile pictures when clicking them on the browser. 
    This opens a small box with the users profile picture they have uploaded.
*/

// Takes in a username, and image path, and checks if that path exists, if it doesn't it sets the path as the default image to fallback on.
function openProfileModal(username, imgUrl) {
    const profileModal = document.getElementById("profile-modal").style.display = "flex";
    const modalImg = document.getElementById("modal-img");
    const modalUsername = document.getElementById("modal-username").innerText = username;

    if (!imgUrl || imgUrl === "None" || imgUrl.includes('undefined')) {
        modalImg.src = "/media/pfp/default.png";
    }
    else {
        modalImg.src = imgUrl;
    }

    modalImg.onerror = function () {
        this.src = "/media/pfp/default.png";
    };
}

function closeProfileModal() {
    document.getElementById("profile-modal").style.display = "none";
}