## 2020年度 プログラミング部

## p5.js 学習

### Step10: コードの整理1 - Ballクラスを作ろう 

* コードをクラスにすることにより、整理することができる。
* [JavaScript クラスの説明サイト(MDN)](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Classes)



##### Class例

```js
class Rectangle {
  // コンストラクタ
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
  
  // メソッド
  calcArea() {
    return this.height * this.width;
  }
}
```



##### クラス(Class)のポイント

* `constructor()` : 最初に呼ばれる初期関数。例では`height`と`width`が引数(argument)として渡されていて、呼び出すときにはこれらを与えなければならない。
* `this.???`というようにクラスが所有している値には`this`をつける。
* メソッド(method) : そのクラスが持っている関数。いわばそのクラスが持っている「動作」のこと。例では`Rectangle`クラスが`calcArea()`というメソッドを持っている。



##### Class 呼び出し例

```js
let square = new Rectangle(10, 10)
console.log(square.calcArea())  // 100が戻される
```



##### クラス初期化(constructor)のポイント

* 例では`square`という変数に初期化した`Rectangle`クラスを代入している。
* 呼び出す時には`new` というキーワードを使用している。
* `Rectangle`クラスには`(10, 10)`というように`height`は10、`width`は10を与えている。
* `square`変数(Rectangleのインスタンス)の中にある`calcArea()`メソッドを呼び出している。
* 例では`console.log()`でコンソールに`calcArea()`の結果を表示している。





#### Task1: Ballクラスを作ろう

##### Hint: 

* 上記の例を参考に、現在あるコード(Step9)をどのように変更できるかを考えよう。
* `Ball`クラスに、`constructor()`初期関数と`show()`と`update()`メソッドを定義しよう。
* `constructor()`
  * `Ball`クラスが所有している値は何なのか？それらを`this.???`で定義する。
* `show()`メソッドは図形を表示するためのもの
  * 図形を表示している関数は何なのか？
* `update()`はフレームごとに呼ばれるためのメソッド
  * フレームごとに変更するもの(変数)は何なのか？
* `edges()`はフレームごとに円が壁に当たっているかを判断し、もしそうなら`speed`変数に-1をかけて逆方向に進ませるためのメソッド

```js
class Ball {
  constructor() {
    this.x = ???
    this.y = ???
    this.speed = ???
  }

  show() {
    circle(???, ???, ???)
  }

  update() {
    this.x = ??? + ???
  }
    
  edges() {
    if (??? && ???) {
    	this.speed = ??? * ???
  	}
    if (??? && ???) {
      this.speed = ??? * ???
    }
  }
}
```





#### Task2: Ballクラスのインスタンスを作り、動かそう

##### Hint: 

* クラスが「家の設計図」だとしたら、インスタンスは「家」
* インスタンスとはクラスを実体化したもの
* `ball`変数をコードの一番上に宣言しよう。
* `setup()`の中に`Ball`を初期化し、インスタンスを作ろう。(`new`キーワードを使うこと)
* `draw()`に新たに作った`ball`インスタンスから`update()`、`edges()`と`show()`メソッドを呼び出そう。



```js
let ball

function setup() {
  createCanvas(400, 400);
  ball = new Ball()
}

class Ball {
  // 上と同じ
}

function draw() {
  background(220);

  ball.???
  ball.???
  ball.???
}
```


#### Task3: Ballクラスに初期値を引数として渡せるようにしよう

##### Hint: 

* `Ball`クラス内の`constructor()`の`()`内に渡したい引数を宣言しよう
* 受け取った引数をクラスの所有する値(`this.???`)に割り当てよう
* 新しくなった`Ball`クラスを初期化し、インスタンスを`ball`変数に割り当てよう


<iframe src="https://editor.p5js.org/sf_/embed/ji8ppQaji"></iframe>


```js
let ball

function setup() {
  createCanvas(400, 400);
  ball = new Ball(200, 150, 7)  // !!! このように初期値を設定できる
}

class Ball {
  constructor(???) {
    this.x = ???
    this.y = ???
    this.speed = ???
  }
  
  // 以下は前と同じ
  // ...

}
```

[sketch](https://editor.p5js.org/sf_/full/ji8ppQaji)
