var btnLogin = document.getElementById("btn");

btnLogin.addEventListener("submit", () => {
    window.location.href = window.Login;
});

function loadPage(url) {
    fetch(url)
        .then((response) => response.text())
        .then((html) => {
            document.body.innerHTML = html;
            feather.replace();
            history.pushState({}, "", url);
        });
}

window.addEventListener("popstate", function (event) {
    loadPage(location.pathname);
});

var btnLogOut = document.getElementById('log-out');

btnLogOut.addEventListener('click', () => {
    window.location.href = window.logOut;
});
