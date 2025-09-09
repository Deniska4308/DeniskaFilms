//обробка кліка по "показати ще"
document.querySelector('.show-all-button').addEventListener('click', () => {
    const actors = document.getElementById("actors");
    const rotateSvg = document.getElementById("rotate-svg");

    actors.classList.toggle('collapsed');
    actors.classList.toggle('expandet');
    rotateSvg.classList.toggle('rotated');

    const buttonText = document.querySelector('.show-all-button span');
    if (actors.classList.contains('collapsed')) {
        buttonText.textContent = 'Показати всіх';
    } else {
        buttonText.textContent = 'Cховати';
    }

});


//для тестів
//для спавну акторів
document.getElementById('actors-test').addEventListener('click', () => {
    const actors = document.getElementById('actors');

    const actorDiv = document.createElement('div');
    actorDiv.classList.add('actor-item');
    
    const actorItem = `
        <div class="actor-img"><img src="static/directors/nophoto-woman.svg" alt=""></div>
        <div class="actor-info text-overflow">
            <span class="text-overflow">Джейн-Енн Тенггрен</span>
            <span class="text-overflow">Jayne-Ann Tenggren </span>
            <span class="text-overflow">55 років</span>
        </div>
    `;

    actorDiv.innerHTML = actorItem;
    actors.appendChild(actorDiv);
});
