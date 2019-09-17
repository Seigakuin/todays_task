# :computer: [聖学院プログラミング部](https://github.com/Seigakuin/todays_task/blob/master/README.md) :computer:

## :game_die: <b> Pygame Zero Project - Dice </b> :game_die:

## 始め方
- ##### このプロジェクトではmu-editorを使い、pythonコードを書きます
    - （すでにPygame Zeroがインストールされているから楽）
- ##### [インストール方法、はじめ方はここから](https://github.com/Seigakuin/todays_task/blob/master/docs/Environment.md)

- ##### [このプロジェクトに必要なアセット(画像ファイル、音声ファイルなど)をダウンロードし、解凍後、ホーム > mu_codeフォルダの中に入れる](https://drive.google.com/open?id=1nIH_3PfIXX2Qh8AQSXWo4ycKp-evsS31&authuser=0)

- ### [Dice 1](https://github.com/Seigakuin/todays_task/blob/master/projects/pygame_zero/dice_project/dice1.py)
    - #### 画面を表示しよう！

- ### [Dice 2](https://github.com/Seigakuin/todays_task/blob/master/projects/pygame_zero/dice_project/dice2.py)
    - #### 画面にテキストを表示しよう！

- ### [Dice 3](https://github.com/Seigakuin/todays_task/blob/master/projects/pygame_zero/dice_project/dice3.py)
    - #### 画面に画像を表示しよう！

- ### [Dice 4](https://github.com/Seigakuin/todays_task/blob/master/projects/pygame_zero/dice_project/dice4.py)
    - #### たくさんの画像をListに入れよう！

- ### [Dice 5](https://github.com/Seigakuin/todays_task/blob/master/projects/pygame_zero/dice_project/dice5.py)
    - #### randomモジュールを使ってランダムにサイコロを表示しよう！

- ### [Dice 6](https://github.com/Seigakuin/todays_task/blob/master/projects/pygame_zero/dice_project/dice6.py)
    - #### キーが押されたらサイコロの数字を変えよう！

- ### [Dice 7](https://github.com/Seigakuin/todays_task/blob/master/projects/pygame_zero/dice_project/dice7.py)
    - #### サイコロの数値を表示しよう！
---
- #### :bug: 日本語を書いてエラーが出た場合...

以下のようなエラー
```python
  File "C:\Users\PC-12\AppData\Local\Mu\pkgs\pgzero\runner.py", line 77, in main
    src = f.read()
UnicodeDecodeError: 'cp932' codec can't decode byte 0x84 in position 28: illegal multibyte sequence
```

直す手順
1. `C:\Users\PC-12\AppData\Local\Mu\pkgs\pgzero\runner.py`にあるファイルをPycharmかIDLEで開く
2. エラーに書いてあるようにline77まで行く
3. 以下のコードを見つける
```python
 with open(path) as f:
        src = f.read()
```
以下のようなコードに書き換える
```python
 with open(path, encoding="utf-8", errors="ignore") as f:
        src = f.read()
```
4. `Adminとして実行しますか`と聞かれるので「はい」と答えて実行する