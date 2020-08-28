let paddle
let ball
let bricks = []
let playingGame = false
let youWin = false
const NUM_BALLS = 60
let winText

function setup() {
  createCanvas(windowWidth, windowHeight)
  paddle = new Paddle()
  ball = new Ball()

  for (let i = 0; i < NUM_BALLS; i++) {
    bricks.push(new Brick())
  }

  createText()
}

function draw() {
  background(255)

  paddle.display()
  if (playingGame) paddle.update()
  if (playingGame) paddle.checkEdges()

  ball.display()
  if (playingGame) ball.update()
  if (playingGame) ball.checkEdges()

  if (ball.meets(paddle) && ball.direction.y > 0) ball.direction.y *= -1

  for (let j = bricks.length - 1; j >= 0; j--) {
    if (ball.hits(bricks[j])) {
      if (bricks[j].r > 40) {
        bricks[j].r = bricks[j].r / 2
      } else {
        bricks.splice(j, 1)
      }
      ball.direction.y *= -1
    }
    if (bricks[j] === undefined) continue
    bricks[j].display()
  }

  if (ball.pos.y > height) {
    playingGame = false
    ball.pos = createVector(width / 2, height / 2)
  }

  if (bricks.length === 0) {
    youWin = true
    playingGame = false
  }

  if (youWin) {
    winText.style("display", "block")
  } else {
    winText.style("display", "none")
  }
}

function keyPressed() {
  if (key === "a" || key === "A") {
    paddle.isMovingLeft = true
  } else if (key === "d" || key === "D") {
    paddle.isMovingRight = true
  } else if (key === "s" || key === "S") {
    playingGame = true
    youWin = false

    if (bricks.length === 0) {
      for (let i = 0; i < 20; i++) {
        bricks.push(new Brick())
      }
    }
  }
}

function keyReleased() {
  paddle.isMovingLeft = false
  paddle.isMovingRight = false
}

function createText() {
  winText = createP("YOU WIN!!!!!!")
  winText.position(width / 2 - 50, 80)
}
