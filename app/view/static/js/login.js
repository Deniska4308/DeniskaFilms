const showPassword = document.querySelector('.show-password-btn');
const password = document.getElementById('password');
showPassword.addEventListener('click', () => {
    showPassword.classList.toggle("show");
    if (password) {
        password.type = password.type === "password" ? "text" : "password";
    };

});