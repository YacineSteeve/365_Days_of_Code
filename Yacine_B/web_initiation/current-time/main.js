const dateSection = document.querySelector('h3');
const timeSection = document.querySelector('h1');

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December'];

function update() {
    const date = new Date();

    const day = days[date.getDay() - 1];
    const month = months[date.getMonth()];
    const fullDate = `${day}, ${month} ${date.getDate()}, ${date.getFullYear()}`

    let minutes = date.getMinutes();
    if (minutes < 10) {
        minutes = '0' + minutes.toString();
    }

    let seconds = date.getSeconds();
    if (seconds < 10) {
        seconds = '0' + seconds.toString();
    }

    let milliseconds = date.getMilliseconds();
    if (milliseconds < 100) {
        milliseconds = '0' + milliseconds.toString()[0];
    } else {
        milliseconds = milliseconds.toString().slice(0, 2);
    }

    const fullTime = `${date.getHours()}:${minutes}:${seconds}.${milliseconds}`;
    dateSection.textContent = fullDate;
    timeSection.textContent = fullTime;
}

window.setInterval(update, 1);
