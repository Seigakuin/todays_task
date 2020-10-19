## <span style="background: #1aafd0">2020年度 プログラミング部</span>

## p5.js 学習

### Step16: Brickをたくさん表示しよう



#### Task: Brickクラスの作成、Ballクラスの調整

##### Hint: 


* `Brick`クラスのプロパティ
* `r`：Brickの一辺の長さ
  * `pos`：`Vector`で位置を表現(`pos`は`square`の左上の角の位置を示す)
  
* `Brick`クラスのメソッド
* `display()`：p5js組み込みの`square`ファンクションを使用する

* `Ball`クラスに`hits`メソッドを追加
  * `ball`の`pos`と`brick`の`pos`を比較し、衝突している場合は`true`を返す

* `setup()`と`draw()`にそれぞれ、新たに`brick`を表示するように調整する

```js
// Step16
let paddle
let ball
// NEW!!
let bricks = []  // brickの配列を格納する
const NUM_BRICKS = 30  // brickができる数

function setup() {
  createCanvas(windowWidth, windowHeight)
  paddle = new Paddle()
  ball = new Ball()


  // NEW!!
  // brickを画面上に作成する
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
  // NEW!!
  hits(brick) {
    // brick.pos はsquareの左上の座標を指す
    // brickの真ん中からのdistanceを得たいため
    // brick.pos.xにbrick.r(サイドｎ長さ)の半分を足し
    // squareの真ん中を指すようにする
    let distance = dist(this.pos.x, this.pos.y, brick.pos.x + brick.r/2, brick.pos.y + brick.r/2)
    if (distance < this.r + brick.r) return true
    else return false
  }
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

// NEW!!
class Brick {
  constructor() {
    this.r = random(20, 80)
    // brickができる初期位置の設定
    // 作成される場所が端っこになりすぎないように100のオフセットを作る
    // brickができる高さは上部から400px下がったところまでにする
    this.pos = createVector(random(100, width - 100), random(100, height - 400))
  }

  display() {
    square(this.pos.x, this.pos.y, this.r)
  }
}


```



# [sketch](https://editor.p5js.org/sf_/sketches/WwuxmLZlZ)




