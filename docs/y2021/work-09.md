##  <span style="background: #1aafd0">2021年度 プログラミング部</span>

## HTML/CSS/Javascript 学習

### Work 09 - 計算機を作ろう！
#### `form`の理解
* 教科書の4-1(p154-180)を読み、以下の画面になるようにコードを書こう！

##### ポイント！
* `input`タグの`type`を`number`にする　`<input type="number" name="num1">`
* 取得した数字はそのままでは文字列なので、数字に変換するために`parseInt()`を使用する
* 

##### 応用！
* 「計算」ボタンを押したあとに`<input>`の中身を消す

<image src="./pics/work-09-01.png" alt="work" width="500" style="border: solid royalblue;" />

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
    <h2>Work 09</h2>
    
    <section>
      <form action="#" id="form">
        <input type="number" name="num1" />
        <input type="number" name="num2" />
        <input type="submit" value="計算" />
      </form>
      <p id="output"></p>
    </section>
    
    
    <script>
      "use strict"
      document.getElementById("form").onsubmit = function (event) {
        console.log("クリックされました。")
        // この下にコードを書こう！
        
      }
    </script>
  </body>
</html>

```



<details>
<summary><b style="font-size: 44px">ヒント</b></summary>
<image src="./pics/work-09-01-hint.png" alt="work" width="500"  />
</details>

