// log_in.js
// The login function retrieves the username and password from the input fields and 
// calls the authenticate function to validate the credentials. If the credentials 
// are correct, it then stores the username in localStorage and brings the user 
// to the myroom.html page. 

function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    authenticate(username, password);
}

function authenticate(username, password) {
    const dummyUsername = "admin";
    const dummyPassword = "password123";

    if (username === dummyUsername && password === dummyPassword) {

        localStorage.setItem("loggedIn", username);

        window.location.href = "myroom.html";
    } else {
        document.getElementById("error").textContent = "Invalid username or password. Please try again.";
    }
}
