/*
    profileChecker.js
    This script checks if a user is logged in by retrieving the username from localStorage. 
    If a user is logged in, it updates the welcome message on the profile page and displays 
    the logout button. The logout button allows the user to log out by removing the username 
    from localStorage and redirecting them to the login page.
*/

function getLoggedInUser() {
    return localStorage.getItem("loggedIn");
}

function updateWelcomeMessage() {
    const user = getLoggedInUser();

    const welcome = document.getElementById("welcome-message");

    if (user && welcome) {
        welcome.textContent = "Hello " + user + "!";
    }
}

function logoutButtonHandler() {
    const user = localStorage.getItem("loggedIn");
    const logoutButton = document.querySelector(".logout");

    if (!logoutButton) return;

    if (user) {
        logoutButton.style.display = "block";

        logoutButton.addEventListener("click", () => {
            localStorage.removeItem("loggedIn");
            window.location.href = "/authenticate/login";
        });

    } else {
        logoutButton.style.display = "none";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    updateWelcomeMessage();
    logoutButtonHandler();
});
