let paddle
let ball
let bricks = []
const NUM_BRICKS = 30

function setup() {
  createCanvas(windowWidth, windowHeight)
  paddle = new Paddle()
  ball = new Ball()

  for (let i = 0; i < NUM_BRICKS; i++) {
    bricks.push(new Brick())
  }
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

  // NEW!!
  // brickの衝突判定
  // brickすべてを確認する
  for (let j = bricks.length - 1; j >= 0; j--) {
    // もしballがbrickに衝突したら
    if (ball.hits(bricks[j])) {
      // もし衝突したbrickの大きさが40px以上だったら
      if (bricks[j].r > 40) {
        // そのbrickの大きさを半分にする
        bricks[j].r = bricks[j].r / 2
      } else {
        // 40px未満だったらそのbrickを消す
        bricks.splice(j, 1)
      }
      // ballが衝突した場合は逆方向に跳ね返す
      ball.direction.y *= -1
    }
    // もしbrickがそこになかったらプログラムを停止せずに
    // 続行する
    if (bricks[j] === undefined) continue
    // brickを表示する
    bricks[j].display()
  }
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
