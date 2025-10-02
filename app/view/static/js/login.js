const showPassword = document.querySelector('.show-password-btn');
const password = document.getElementById('password');
showPassword.addEventListener('click', () => {
    showPassword.classList.toggle("show");
    if (password) {
        password.type = password.type === "password" ? "text" : "password";
    };

});




document.getElementById('login').addEventListener('submit', async (e) => {
    e.preventDefault();
    const f = e.target;

    const body = {
        "username": f.username.value,
        "password": f.password.value
    };

    const res = await fetch('http://127.0.0.1:8000/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(body)
    });
    console.log(res)
});
