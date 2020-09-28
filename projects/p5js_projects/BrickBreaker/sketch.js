let paddle

function setup() {
  createCanvas(windowWidth, windowHeight)
  // Paddleクラスのインスタンスを作成
  paddle = new Paddle()
}

function draw() {
  background(255)

  // Paddleインスタンスのdisplay(), update(), checkEdges()を呼び出す（繰り返し）
  paddle.display()
  paddle.update()
  paddle.checkEdges()
}

function keyPressed() {
  if (key === "a" || key === "A") {
    // キーボードのaもしくはAが押された時にPaddleインスタンスのi isMovingRight を true に変更
    paddle.isMovingLeft = true
  } else if (key === "d" || key === "D") {
    // キーボードの d もしくは D が押された時にPaddleインスタンスのi isMovingLeft を true に変更
    paddle.isMovingRight = true
  }
}

function keyReleased() {
  // キーボードのキーを押しているのを離したら Paddleインスタンスの isMovingLeft, isMovingRight を false に変更
  paddle.isMovingLeft = false
  paddle.isMovingRight = false
}

class Paddle {
  constructor() {
    this.w = 160 // w = 幅
    this.h = 20 // h = 高さ

    this.isMovingLeft = false // 左に動いているか Boolean
    this.isMovingRight = false // 右に動いているか Boolean

    // pos = 位置を示すVector
    this.pos = createVector(width / 2, height - 40)
  }

  display() {
    // 長方形を表示
    rect(this.pos.x, this.pos.y, this.w, this.h)
  }

  move(step) {
    // 動きを司る関数 pos.x （横位置） に 引数として渡す step の量を動かす
    this.pos.x += step
  }

  update() {
    if (this.isMovingRight) {
      // もし、 isMovingRight が true だとしたら右に 20ピクセル動かす
      this.move(20)
    } else if (this.isMovingLeft) {
      // もし、 isMovingLeft が true だとしたら左に 20ピクセル動かす
      this.move(-20)
    }
  }

  checkEdges() {
    // 画面外に移動しないように工夫
    if (this.pos.x < 0) {
      // もし、pos.x の位置が左画面外に移動したら、位置を画面左端に戻す
      this.pos.x = 0
    } else if (this.pos.x > width - this.w) {
      // もし、Paddleの右端が画面右端に移動したら、位置を画面右端に戻す
      // ＊ pos.xはPaddleの左上の位置を示すので、右端を計算するにはPaddleの幅を足して計算をしなければならない
      this.pos.x = width - this.w
    }
  }
}
