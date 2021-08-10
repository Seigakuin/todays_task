##  <span style="background: #1aafd0">2021年度 プログラミング部</span>

## HTML/CSS/Javascript 学習

### Work 04 - FizzBuzzFooBar functionを作ろう！ 
#### `function`の理解
* 教科書の3-9(p118-122)を読み、以下の画面になるように`function`を使ったコードを書こう！

##### FizzBuzzFooBar functionの条件
1. 2でも3でも5でも7でも割り切れる場合は「FizzBuzzFooBar」をリターンとして返す
2. 3でも5でも7でも割り切れる場合は「FizzBuzzFoo」をリターンとして返す
3. 3でも5でも割り切れる場合は「FizzBuzz」をリターンとして返す
4. 7で割り切れる場合は「Bar」をリターンとして返す
5. 5で割り切れる場合は「Foo」をリターンとして返す
6. 3で割り切れる場合は「Buzz」をリターンとして返す
7. 2で割り切れる場合は「Fizz」をリターンとして返す
8. それ以外は渡された数値をそのままリターンとして返す

<image src="./pics/work-04-01.png" alt="house" width="300"  />

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
    <h2>Work 04</h2>
    <script>
      "use strict"

      function myFizzBuzzFooBar(num) {
        //ここにコードを書く!
      }

      let i = 1

      while (i <= 300) {
        console.log(myFizzBuzzFooBar(i))
        i += 1
      }
    </script>
  </body>
</html>

```


