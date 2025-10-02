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


//обробка реэстрації
document.getElementById('registerForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const f = e.target;

    const body = {
        "email": f.mail.value || null,
        "username": f.username.value,
        "password": f.password.value
    };
    console.log(f.mail.value);
    const res = await fetch('http://127.0.0.1:8000/register', {
        method:'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(body)
    });

    
    const data = await res.json();
});



// document.getElementById('ActorForm').addEventListener('submit', async (e) => {
//     e.preventDefault();
//     const f = e.target;
//     const body = {
//         name: f.actor_name.value,
//         true_name: f.actor_true_name.value,
//         birth_date: f.actor_birth_date.value || null,
//         photo_url: f.actor_photo_url.value || null
//     };

//     const res = await fetch('http://127.0.0.1:8000/api/movie/actor', {
//         method: 'POST',
//         headers: {'Content-Type': 'application/json'},
//         body: JSON.stringify(body)
//     });
//     const data = await res.json();
    
    // updateLog(data);
    // console.log(data);
// });
