## <span style="background: #00acee">2020年度 プログラミング部</span>

## p5.js 学習

### Step12: Ballを上下左右の壁から跳ね返るようにしよう

* `NUM_BALLS`変数でボールの数を管理しよう(この数字を変えることでボールの数を管理できるから便利)
* `Ball`クラス`speed`プロパティを`xspeed`と`yspeed`に分けて管理する
* `Ball`クラスの`edges()`メソッドに新たに上下の壁に衝突した時の挙動を書く
* `Ball`クラスの`update()`メソッドに`yspeed`に対応するコードを追加する



#### Task: Ballを上下左右の壁から跳ね返るようにしよう

##### Hint: 
* `width`と`height`は画面の大きさを取得してくれる変数
* `Ball`の引数はすべて`random()`で生成
* 上下の壁から`Ball`が跳ね返るように`edges()`メソッドにコードを追記する



```js
let balls = []
const NUM_BALLS = ???  // NUM_BALLS変数でボールの数を管理

function setup() {
  createCanvas(400, 400);

  // !! ここでBallインスタンスを作成
  for (let i = 0; i < ???; i++) {
    // Ballがランダムな大きさ
    balls.push(new Ball(
      random(10, width),  // x 
      random(0, height),  // y
      ???,  // r 直径
      ???,  // xspeed 
      ???  // yspeed
    ))
  }
}

class Ball {
  constructor(x, y, r, xspeed, yspeed) {
    this.x = x
    this.y = y
    this.r = r
    // 縦の動きを加える yspeed (speedをxspeedに変更)
    this.xspeed = xspeed
    this.yspeed = yspeed
  }

  show() {
    circle(this.x, this.y, this.r)
  }

  update() {
    this.x = this.x + this.xspeed
    this.y = this.y + this.yspeed
  }

  edges() {
    
    if (this.x >= 400 && this.xspeed > 0) {
      this.xspeed = this.xspeed * -1
    }
    if (this.x < 0 && this.xspeed < 0) {
      this.xspeed = this.xspeed * -1
    }
    // 上下の壁からも跳ね返るようにする
    if (??? && ???) {
      this.yspeed = this.yspeed * -1
    }
    if (??? && ???) {
      this.yspeed = this.yspeed * -1
    }
  }
}

function draw() {
  background(220);

  // !! ここでBallを描く
  for (let i = 0; i < ???; i++) {
    balls[i].update()
    balls[i].edges()
    balls[i].show()
  }
}
```

![step12](pics/step12.png)



# [sketch](https://editor.p5js.org/sf_/sketches/rtvBWovEO)