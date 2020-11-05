## <span style="background: #1aafd0">2020年度 プログラミング部</span>

## p5.js 学習

### Step18: 雪をたくさん降らせよう



#### Task: たくさん雪を表示する

##### Hint: 
* `circleY`: `circle`のY座標を配列（array）に格納
* `circleX` : `circle`のX座標を重ならないように工夫をする

```js
// Step18
// たくさんのY座標をarrayに格納
let circleY = [???...];

function setup() {
  createCanvas(300, 300);
}

function draw() {
  background(50);

  // 雪をforループで一つひとつを表示
  for (???; ???; ???) {
    // circleのX座標を設定（＊同じ場所にならないように工夫！）
    let circleX = ???;
       
    // circleを描く
    circle(???, ???, ???);

  	// circleを下に動かす
    ???;
    
  	// circleが下についたら上に戻す
    if (??? > ???) {
      ???;
    }
  }
}


```

![step13](pics/task18.png)

# [sketch](https://editor.p5js.org/sf_/present/HDnVcAZac)




