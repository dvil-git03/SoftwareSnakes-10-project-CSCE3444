function createNewUser() {
    const email = document.getElementById("email").value;
    const name = document.getElementById("name").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    authenticate(email, username);
}

function authenticate(email, username) {
//check if email and username are already used
}