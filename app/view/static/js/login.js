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
    if(res.status == 401) {
        const message = `<p>Логін або пароль невірні</p>`;
        var mess = document.getElementById("mess");
        mess.innerHTML = message;
    }else if(res.status == 200) {
        var mess = document.getElementById("mess").innerHTML = ``
        window.location.href = "/"
    };

})
