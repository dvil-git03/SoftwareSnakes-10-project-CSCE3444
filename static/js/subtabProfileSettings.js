/*
    subtabProfileSettings.js
    This script adds event listeners to the "My Profile" and "Settings" buttons in the 
    sidebar of the profile and settings pages. When a button is clicked, it redirects 
    the user to the corresponding page (profile.html or settings.html).
*/

window.addEventListener("DOMContentLoaded", () => {
    const profileButton = document.getElementById("nav-profile");
    const settingsButton = document.getElementById("nav-settings");

    if (profileButton) {
        profileButton.addEventListener("click", () => {
            window.location.href = "/users/profile";
        });
    }
    if (settingsButton) {
        settingsButton.addEventListener("click", () => {
            window.location.href = "/users/settings";
        });
    }
});
