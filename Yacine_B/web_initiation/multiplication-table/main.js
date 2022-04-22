const inputZone = document.querySelector('input');
const displayButton = document.querySelector('button');
const displayZone = document.querySelector('ul');

inputZone.focus();


function generateTable() {
    let lines = document.querySelectorAll('li');
    const value = Number(inputZone.value);
    
    for (const line of lines) {
        displayZone.removeChild(line);
    }
    
    if (isNaN(value)) {
        let line = document.createElement('li');
        
        line.textContent = 'Saisie invalide! Veuillez entrer un nombre.';
        displayZone.appendChild(line);
    } else {
        for (let i = 0; i < 13; i++) {
            let line = document.createElement('li');
            
            line.textContent = `${value} x ${i} = ${value * i}`;
            displayZone.appendChild(line);
        }
    }
}


displayButton.onclick = generateTable;

window.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        generateTable();
    }
})
