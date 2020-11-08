## <span style="background: #1aafd0">2020年度 プログラミング部</span>

## p5.js 学習

### Step17: 雪を降らせよう



#### Task: 雪を画面に出現させる

##### Hint: 
* 

```js
// Step17
let snowList = []  // Snowインスタンスを格納する配列

function setup() {
  createCanvas(400, 400)
}

function draw() {
  background(0)
  snowList.???(new ???()) // Snowインスタンスを作成

  // snowList配列の中にある、一つずつsnowとして取り出す
  for (let snow of snowList) {
    snow.???()
  }
}

class Snow {
  constructor() {
    let x = random(width) // x位置をランダムに設定
    let y = random(height) // y位置をランダムに設定
    this.pos = createVector(x, y) // 位置Vectorのプロパティ
  }

  draw() {
    stroke(255) // 色は白
    strokeWeight(4) // pointの大きさは４
    point(???, ???)
  }
}




```
![step13](pics/task17.png)


# [sketch](https://editor.p5js.org/sf_/present/ERbQ90Zqf)




