document.getElementById("btn").addEventListener('submit', () => {
    window.location.href = window.Login;
});

document.getElementById("checkPw").addEventListener("click", () => {
    const password = document.getElementById("password");
    if (password.type === "password") {
        password.type = "text";
    } else {
        password.type = "password";
    }
});
