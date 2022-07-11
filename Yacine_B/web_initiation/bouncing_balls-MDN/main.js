const canvas = document.querySelector('canvas')
const ctx = canvas.getContext('2d')

const width = canvas.width = window.innerWidth
const height = canvas.height = window.innerHeight

/**
 * Return a random number between min and max values.
 * @param  {Number} min - The minimum value.
 * @param  {Number} max - The maximum value.
 * @return {Number}     - A number between min and max.
 */
function random (min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min
}

/**
 * Generate a random RGB color.
 * @returns {String} - A color with rgb format.
 */
function randomColor () {
  return 'rgb(' + random(0, 255) + ',' + random(0, 255) + ',' + random(0, 255) + ')'
}

/**
 * Represent a shape on the canvas.
 * @param {Number}  posX   - The position of the shape about axis X.
 * @param {Number}  posY   - The position of the shape about axis Y.
 * @param {Number}  speedX - The speed of the shape about axis X.
 * @param {Number}  speedY - The speed of the shape about axis Y.
 * @param {Boolean} exists - Whether the shape exists or not.
 * @constructor
 */
function Shape (posX, posY, speedX, speedY, exists) {
  this.posX = posX
  this.posY = posY
  this.speedX = speedX
  this.speedY = speedY
  this.exists = exists
}

/**
 * Representing a ball.
 * @param {Number}  posX   - The position of the ball about axis X.
 * @param {Number}  posY   - The position of the ball about axis Y.
 * @param {Number}  speedX - The speed of the ball about axis X.
 * @param {Number}  speedY - The speed of the ball about axis Y.
 * @param {Boolean} exists - Whether the ball exists or not.
 * @param {String}  color  - The ball color (can be explicit, rgb or rgba).
 * @param {Number}  size   - The ball radius.
 * @constructor
 */
function Ball (posX, posY, speedX, speedY, exists, color, size) {
  Shape.call(this, posX, posY, speedX, speedY, exists)
  this.color = color
  this.size = size
}

Ball.prototype = Object.create(Shape.prototype)
Ball.prototype.constructor = Ball

Ball.prototype.draw = function () {
  ctx.beginPath()
  ctx.fillStyle = this.color
  ctx.arc(this.posX, this.posY, this.size, 0, 2 * Math.PI)
  ctx.fill()
}

Ball.prototype.updateBall = function () {
  if (this.posX + this.size >= width || this.posX - this.size <= 0) {
    this.speedX = -(this.speedX)
  }

  if (this.posY + this.size >= height || this.posY - this.size <= 0) {
    this.speedY = -(this.speedY)
  }

  this.posX += this.speedX
  this.posY += this.speedY
}

Ball.prototype.collisionDetect = function () {
  for (let i = 0; i < balls.length; i++) {
    if (balls[i].exists && !(this === balls[i])) {
      const dx = this.posX - balls[i].posX
      const dy = this.posY - balls[i].posY
      const distance = Math.sqrt(dx * dx + dy * dy)

      if (distance < this.size + balls[i].size) {
        balls[i].color = this.color = randomColor()
      }
    }
  }
}

/**
 * Represent the visor that will be used to destroy the balls.
 * @param {Number}  posX   - The position of the visor about axis X.
 * @param {Number}  posY   - The position of the visor about axis Y.
 * @constructor
 */
function Visor (posX, posY) {
  Shape.call(this, posX, posY, 20, 20, true)
  this.color = 'white'
  this.size = 10
}

Visor.prototype = Object.create(Shape.prototype)
Visor.prototype.constructor = Visor

Visor.prototype.draw = function () {
  ctx.beginPath()
  ctx.arc(this.posX, this.posY, this.size, 0, 2 * Math.PI)
  ctx.lineWidth = 2
  ctx.strokeStyle = this.color
  ctx.moveTo(this.posX, this.posY - 0.5 * this.size)
  ctx.lineTo(this.posX, this.posY - 1.5 * this.size)
  ctx.moveTo(this.posX, this.posY + 0.5 * this.size)
  ctx.lineTo(this.posX, this.posY + 1.5 * this.size)
  ctx.moveTo(this.posX - 0.5 * this.size, this.posY)
  ctx.lineTo(this.posX - 1.5 * this.size, this.posY)
  ctx.moveTo(this.posX + 0.5 * this.size, this.posY)
  ctx.lineTo(this.posX + 1.5 * this.size, this.posY)
  ctx.stroke()
}

Visor.prototype.collisionDetect = function () {
  for (let i = 0; i < balls.length; i++) {
    if (balls[i].exists) {
      const dx = this.posX - balls[i].posX
      const dy = this.posY - balls[i].posY
      const distance = Math.sqrt(dx * dx + dy * dy)

      if (distance < balls[i].size + 0.5 * this.size) {
        balls[i].exists = false
      }
    }
  }
}

const visor = new Visor(width / 2, height / 2)
const balls = []
const initialBallsNumber = 15
const minSpeed = -7
const maxSpeed = 7

while (balls.length < initialBallsNumber) {
  const size = random(10, 20)
  const ball = new Ball(
    random(size, width - size),
    random(size, height - size),
    random(minSpeed, maxSpeed),
    random(minSpeed, maxSpeed),
    true,
    randomColor(),
    size
  )

  balls.push(ball)
}

/**
 * @returns {Number} - The number of balls with exists property value at true.
 */
function countBalls () {
  let count = 0
  for (let i = 0; i < balls.length; i++) {
    if (balls[i].exists) {
      count += 1
    }
  }
  return count
}

function loop () {
  const ballsNumber = countBalls()
  const scoreText = 'Balls remaining : ' + ballsNumber.toString() + '/' + initialBallsNumber.toString()

  ctx.fillStyle = 'rgba(0, 0, 0, 0.4)'
  ctx.fillRect(0, 0, width, height)

  ctx.font = '20px Arial'
  ctx.fillStyle = 'white'
  ctx.fillText(scoreText, 50, 50)

  if (ballsNumber === 0) {
    ctx.font = '100px Ubuntu'
    ctx.fillStyle = 'green'
    ctx.fillText('Victoire !!', width / 2.75, height / 2.5)
  }

  for (let i = 0; i < balls.length; i++) {
    if (balls[i].exists) {
      balls[i].draw()
      balls[i].updateBall()
      balls[i].collisionDetect()
    }
  }

  visor.draw()
  visor.collisionDetect()

  requestAnimationFrame(loop)
}

window.addEventListener('keydown', (event) => {
  switch (event.key) {
    case 'ArrowUp':
    case 'z':
    case 'Z':
    {
      if (visor.posY - visor.speedY >= 1.5 * visor.size) {
        visor.posY -= visor.speedY
      }
      break
    }
    case 'ArrowDown':
    case 's':
    case 'S':
    {
      if (visor.posY + visor.speedY <= height - 1.5 * visor.size) {
        visor.posY += visor.speedY
      }
      break
    }
    case 'ArrowLeft':
    case 'q':
    case 'Q':
    {
      if (visor.posX - visor.speedX >= 1.5 * visor.size) {
        visor.posX -= visor.speedX
      }
      break
    }
    case 'ArrowRight':
    case 'd':
    case 'D':
    {
      if (visor.posX + visor.speedX <= width - 1.5 * visor.size) {
        visor.posX += visor.speedX
      }
      break
    }
    default: {
      break
    }
  }
})

loop()
