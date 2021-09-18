##  <span style="background: #1aafd0">2021年度 プログラミング部</span>

## HTML/CSS/Javascript 学習

### Work 08 - オブジェクトを使って複数の生徒情報を表示しよう！
#### `object`の理解
* 教科書の3-11(p138-152)を読み、以下の画面になるようにコードを書こう！

##### ポイント！
* p147にある`for...in`文を確認
* `jsbook.p`ではなく、`jsbook[p]`という表記でないと`for .. in`文の中では読み取れないよ。

##### 応用！
* `for ... of`文を使っても同じことが表現できるから余裕がある人はためしてみて！

<image src="./pics/work-08-01.png" alt="work" width="500" style="border: solid royalblue;" />

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
    <h2>Work 07</h2>
    <script>
      "use strict"
      let students = [
        {
          name: "Seigakuin Taro",
          homeroom: "C",
          num: 31,
        },
        {
          name: "Seigakuin Jiro",
          homeroom: "B",
          num: 14,
        },
        {
          name: "Seigakuin Saburo",
          homeroom: "B",
          num: 19,
        },
      ]
      // この下にコードを書こう！

    </script>
  </body>
</html>

```



<details>
<summary><b style="font-size: 44px">ヒント</b></summary>
<image src="./pics/work-08-01-hint.png" alt="work" width="500"  />
</details>

