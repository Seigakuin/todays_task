## <span style="background: #00acee">2020年度 プログラミング部</span>

## p5.js 学習

### Step12: Ballを上下左右の壁から跳ね返るようにしよう

* `NUM_BALLS`変数でボールの数を管理しよう(この数字を変えることでボールの数を管理できるから便利)
* `Ball`クラス`speed`プロパティを`xspeed`と`yspeed`に分けて管理する
* `Ball`クラスの`edges()`メソッドに新たに上下の壁に衝突した時の挙動を書く
* `Ball`クラスの`update()`メソッドに`yspeed`に対応するコードを追加する











#### Task: 

##### Hint: 


* 



```js
let balls = []

function setup() {
  createCanvas(400, 400);

  // !! ここでBallインスタンスを作成
  for (???; ???; ???) {
    balls.push(new Ball(
      random(???, ???),
      random(???, ???),
      random(???, ???)
    ))
  }
}

class Ball {
  // ここは以前と同じ
}

function draw() {
  background(220);

  // !! ここでBallを描く
  for (???; ???; ???) {
    ???.update()
    ???.edges()
    ???balls[i].show()
  }
}
```

![step8-2](pics/step11.png)

