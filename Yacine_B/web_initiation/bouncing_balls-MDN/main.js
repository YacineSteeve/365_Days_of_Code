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

/**
 * Generate a random RGB color.
 * @returns {String} - A color with rgb format.
 */
function randomColor() {
    return 'rgb(' + random(0, 255) + ',' + random(0, 255) + ',' + random(0, 255) +')';
}

/**
 * A constructor representing a ball.
 * @param {Number} posX   - The position of the ball about axis X.
 * @param {Number} posY   - The position of the ball bout axis Y.
 * @param {Number} speedX - The speed of the ball about axis X.
 * @param {Number} speedY - The speed of the ball about axis Y.
 * @param {String} color  - The ball color (can be explicit, rgb or rgba).
 * @param {Number} size   - The ball radius.
 * @constructor
 */
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

Ball.prototype.updateBall = function() {
    if (this.posX + this.size >= width || this.posX - this.size <= 0) {
        this.speedX = -(this.speedX);
    }
    
    if (this.posY + this.size >= height || this.posY - this.size <= 0) {
        this.speedY = -(this.speedY);
    }
    
    this.posX += this.speedX;
    this.posY += this.speedY;
};

Ball.prototype.collisionDetect = function() {
    for (let i = 0; i < balls.length; i++) {
        if (!(this === balls[i])) {
            const dx = this.posX - balls[i].posX;
            const dy = this.posY - balls[i].posY;
            const distance = Math.sqrt(dx * dx + dy * dy);

            if (distance <= this.size + balls[i].size) {
                balls[i].color = this.color = randomColor();
            }
        }
    }
};


let balls = [];
const ballsNumber = 15;
const minSpeed = -7;
const maxSpeed = 7;

while (balls.length < ballsNumber) {
    let size = random(10, 30);
    let ball = new Ball(
        random(size, width - size),  // To avoid drawing outside the canvas.
        random(size, height - size), // Same.
        random(minSpeed, maxSpeed), 
        random(minSpeed, maxSpeed), 
        randomColor(),
        size
    );

    balls.push(ball);
}

function loop() {
    context.fillStyle = 'rgba(0, 0, 0, 0.25)';
    context.fillRect(0, 0, width, height);

    for (let i = 0; i < balls.length; i++) {
        balls[i].draw();
        balls[i].updateBall();
        balls[i].collisionDetect();
    }

    requestAnimationFrame(loop);
}

loop();
