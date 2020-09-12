##  <span style="background: #ffb900">2020年度 プログラミング部</span>

## p5.js 学習

### Step9: 円を動かそう 

* `draw()`関数はペラペラ漫画のように１秒間に60回(フレームレート: 60fps)ほど呼び出される。1回で呼ばれるごとに映像に少しずつ変化をつければアニメーションになる。
* コードの一番上に変化し続ける変数を設定しよう。`let xchange = 0`
* `xchange`変数を`draw()`関数の中で変化させよう。`xchange = xchange + 1` (1は速度に値する)

```js
let xchange = 0

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  
  circle(xchange, 200, 100)
  
  xchange = xchange + 1
}
```

#### Task: 円を斜めに動かそう

* 上記のコードに新たに`ychange`という変数を作り、円が斜めに動くようなコードを作成しよう。



---


### Step10: if文を理解しよう

* 

* if文

```js
if ([条件1]) {
  // 条件に合えば実行する文
} else if ([条件2]) {
  // 条件に合えば実行する文
} else {
  // どの条件にも合わない場合、実行される文
}
```

* if文例

```js
if (x < 10) {
  console.log("数字は10未満です。")
} else if (x >= 5) {
  console.log("数字は10未満かつ、5以上です。")
} else {
  console.log("数字は10以上、もしくは4以下です。")
}
```



#### Task: 円が画面外に出てしまったら、再び画面左から登場するように条件(if)を設定しよう

##### Hint: 

* `xchange` が画面外に出るということはどの値になってしまうのかを考えよう。
* `xchange`が画面外にでたら、どの数値を入れれば画面左に戻るのかを考えよう。

```js
let xchange = 0

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  
  circle(xchange, 200, 100)
  
  if (???) {
    ??? 
  }
  
  xchange = xchange + 1
}
```



#### Task: 円が壁から跳ね返るようにしよう

##### Hint: 

* `speed`変数を作り、円が進む方向に割り当てよう
* `&&` は複数の条件が合う時に使う (`AND`と同じ意味) 

```js
let xchange = 0
let speed = ???

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  
  circle(xchange, 200, 100)
  
  // && は「かつ」という意味
  if (?[ここは上のコードと同じ]? && speed ? ???) {
    ??? = ??? * ???
  }
  
  if (?[ここは上のコードと同じ]? && speed ? ???) {
    ??? = ??? * ???
  }
  
  xchange = xchange + speed
}
```



