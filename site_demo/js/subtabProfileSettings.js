/*
    subtabProfileSettings.js
    This script adds event listeners to the "My Profile" and "Settings" buttons in the 
    sidebar of the profile and settings pages. When a button is clicked, it redirects 
    the user to the corresponding page (profile.html or settings.html).
*/

window.addEventListener("DOMContentLoaded", () => {
    const profileBtn = document.getElementById("nav-profile");
    const settingsBtn = document.getElementById("nav-settings");

    if (profileBtn) {
        profileBtn.addEventListener("click", () => {
            window.location.href = "profile.html";
        });
    }
    if (settingsBtn) {
        settingsBtn.addEventListener("click", () => {
            window.location.href = "settings.html";
        });
    }
});
