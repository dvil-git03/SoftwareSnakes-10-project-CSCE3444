// profileForm.js
// This script populates the profile form with the user's information when the 
// profile page is loaded. It retrieves the logged-in user's username from 
// localStorage and uses it to  access a dummy user data object. The user's email, 
// name, username, and password are then filled into the corresponding input fields 
// in the profile form.

window.addEventListener("DOMContentLoaded", () => {
    const user = localStorage.getItem("loggedIn");

    const users = {
        "admin": {
            email: "fake-email@gmail.com",
            name: "Admin Schmadmin",
            username: "admin",
            password: "password123"
        }
    };

    const userData = users[user];

    if (!userData) return;

    document.getElementById("email").value = userData.email;
    document.getElementById("name").value = userData.name;
    document.getElementById("username").value = userData.username;
    document.getElementById("password").value = userData.password;

});
