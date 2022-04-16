const canvas = document.querySelector('canvas');
const context = canvas.getContext('2d');

const width = canvas.width = window.innerWidth;
const height = canvas.height = window.innerHeight;

/**
 * Return a random number between min and max values.
 * @param  {Number} min - The minimum value.
 * @param  {Number} max - The maximum value.
 * @return {Number}     - A number between min and max.
 */
function random(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function Ball(posX, posY, speedX, speedY, color, size) {
    this.posX = posX;
    this.posY = posY;
    this.speedX = speedX;
    this.speedY = speedY;
    this.color = color;
    this.size = size;
}

Ball.prototype.draw = function() {
    context.beginPath();
    context.fillStyle = this.color;
    context.arc(this.posX, this.posY, this.size, 0, 2 * Math.PI);
    context.fill();
};

Ball.prototype.update = function() {
    if (this.posX + this.size >= width || this.posX - this.size <= 0) {
        this.speedX = -(this.speedX);
    }
    
    if (this.posY + this.size >= height || this.posY - this.size <= 0) {
        this.speedY = -(this.speedY);
    }
    
    this.posX += this.speedX;
    this.posY += this.speedY;
};
