let paddle
let ball

function setup() {
  createCanvas(windowWidth, windowHeight)
  paddle = new Paddle()
  ball = new Ball()
}

function draw() {
  background(255)

  paddle.display()
  paddle.update()
  paddle.checkEdges()

  ball.display()
  ball.update()
  ball.checkEdges()

  if (ball.meets(paddle) && ball.direction.y > 0) ball.direction.y *= -1
}

function keyPressed() {
  if (key === "a" || key === "A") {
    paddle.isMovingLeft = true
  } else if (key === "d" || key === "D") {
    paddle.isMovingRight = true
  }
}

function keyReleased() {
  paddle.isMovingLeft = false
  paddle.isMovingRight = false
}

class Paddle {
  constructor() {
    this.w = 160
    this.h = 20

    this.isMovingLeft = false
    this.isMovingRight = false

    this.pos = createVector(width / 2, height - 40)
  }

  display() {
    rect(this.pos.x, this.pos.y, this.w, this.h)
  }

  move(step) {
    this.pos.x += step
  }

  update() {
    if (this.isMovingRight) {
      this.move(20)
    } else if (this.isMovingLeft) {
      this.move(-20)
    }
  }

  checkEdges() {
    if (this.pos.x < 0) this.pos.x = 0
    else if (this.pos.x > width - this.w) this.pos.x = width - this.w
  }
}

class Ball {
  constructor() {
    this.pos = createVector(width / 2, height / 2)
    this.r = 30

    this.direction = createVector(1, 1)
    this.vel = createVector(1, 1).mult(5)
  }

  display() {
    ellipse(this.pos.x, this.pos.y, this.r * 2, this.r * 2)
  }

  update() {
    this.pos.x += this.vel.x * this.direction.x
    this.pos.y += this.vel.y * this.direction.y
  }

  checkEdges() {
    if (this.pos.y < this.r && this.direction.y < 0) this.direction.y *= -1

    // if (this.pos.y > height - this.r && this.direction.y > 0) this.direction.y *= -1

    if (this.pos.x < this.r && this.direction.x < 0) this.direction.x *= -1

    if (this.pos.x > width - this.r && this.direction.x > 0)
      this.direction.x *= -1
  }

  meets(paddle) {
    if (
      this.pos.y < paddle.pos.y &&
      this.pos.y > paddle.pos.y - this.r &&
      this.pos.x > paddle.pos.x - this.r &&
      this.pos.x < paddle.pos.x + paddle.w + this.r
    ) {
      return true
    } else return false
  }
}
