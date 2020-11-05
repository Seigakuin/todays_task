## <span style="background: #1aafd0">2020年度 プログラミング部</span>

## p5.js 学習

### Step17: 雪を降らせよう



#### Task: 1粒の雪をループで表示する

##### Hint: 
* `circleY`: `circle`のY座標を格納

```js
// Step17
let circleY = 0;

function setup() {
  createCanvas(300, 300);
}

function draw() {
  background(50);

  // circleを描く
  circle(???, ???, ???);
  // circleを下方向にすすめる
  ???;
  // circleが下まで行ったら、上に戻す
  if (??? > ???) {
    circleY = ???;
  }
}


```
![step13](pics/task17.png)


# [sketch](https://editor.p5js.org/sf_/present/ERbQ90Zqf)




