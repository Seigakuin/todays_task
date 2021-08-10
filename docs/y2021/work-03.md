##  <span style="background: #1aafd0">2021年度 プログラミング部</span>

## HTML/CSS/Javascript 学習

### Work 03 - 占いページを作ろう！ 
#### `function`の理解
* 教科書の3-8(p110-117)を読み、以下の画面になるように`function`を使ったコードを書こう！

<image src="./pics/work-03-01.png" alt="house" width="300"  />

<br></br>

以下のコードから始めても良い

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>SEIGAKUIN PROGRAMMING CLUB</title>
  </head>
  <body>
    <h1>SEIGAKUIN PROGRAMMING CLUB</h1>
    <h2>Work 03</h2>
    <script>
      "use strict"
      const color = window.prompt("色を選んでください！(青, 黄色, 赤, 緑)")

      function uranai(color) {
        // ここにコードを書こう！
      }
      document.getElementById("output").textContent =
        "今日のあなたの運命は" + uranai(color) + "です！"
    </script>
  </body>
</html>

```


