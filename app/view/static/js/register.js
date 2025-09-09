//діви з тим оком
const showPassword = document.getElementById('show-password-btn');
const showAceptPassword = document.getElementById('show-acept-password-btn');

// інпут поля для паролів
const password = document.getElementById('password');
const acept_password = document.getElementById('acept-password');

// обробка кліку попершого поля
showPassword.addEventListener('click', () => {
    showPassword.classList.toggle("show");
    showAceptPassword.classList.toggle("show")
    if (password || acept_password) {
        password.type = password.type === "password" ? "text" : "password";
        acept_password.type = acept_password.type === "password" ? "text" : "password";
    };
});
// обробка кліку дрогого поля поля
showAceptPassword.addEventListener('click', () => {
    showPassword.classList.toggle("show");
    showAceptPassword.classList.toggle("show")
    if (password || acept_password) {
        password.type = password.type === "password" ? "text" : "password";
        acept_password.type = acept_password.type === "password" ? "text" : "password";
    };
});