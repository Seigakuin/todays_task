##  <span style="background: #1aafd0">2021年度 プログラミング部</span>

## HTML/CSS/Javascript 学習

### Work 07 - オブジェクトを使って生徒情報を表示しよう！
#### `object`の理解
* 教科書の3-11(p138-152)を読み、以下の画面になるようにコードを書こう！

##### ポイント！
* p140にあるオブジェクトのデータの呼び出し方を確認
* テンプレート文字列がまだ曖昧な人は、p131-133を復習


<image src="./pics/work-07-01.png" alt="work" width="500" style="border: solid royalblue;" />

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
       let homeroom = "C"

      let student = {
        name: "Seigakuin Taro",
        homeroom: "C",
        num: 31,
      }
      console.log(`${homeroom}組の生徒情報`)
      // この下にコードを書こう！

    </script>
  </body>
</html>

```




<details>
<summary><b style="font-size: 44px">ヒント</b></summary>
<image src="./pics/work-07-01-hint.png" alt="work" width="500"  />
</details>

