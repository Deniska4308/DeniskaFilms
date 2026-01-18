const showPassword = document.querySelector('.show-password-btn');
const password = document.getElementById('password');
showPassword.addEventListener('click', () => {
    showPassword.classList.toggle("show");
    if (password) {
        password.type = password.type === "password" ? "text" : "password";
    };

});

//оброька реєстрації (хулі тут такого не було?)
document.getElementById('login').addEventListener('submit', async (e) => {
    e.preventDefault();
    const f = e.target;
    const body = {
        "username": f.password.value,
        "password": f.username.value
    }
    console.log(f.username.value)

    const res = await fetch('/login', {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
        credentials: "include"
    })

    //logs
    if(!res.ok) {
        const err = await res.json().catch(() => ({}));
        console.log(err.detail || "Login failed");
        console.log(res.status || "Login failed");
        return;
    }
})
