### mu-editor始め方
#### インストール
- [mu-editorホームページ](https://codewith.mu)に行き"Download"をクリック
- "Windows Installer" "64-bit" をクリックするとダウンロードが開始される

#### 始め方
- "Windowsマーク"(画面左下)から"mu-editor"を選ぶ
- 画面が開き、"モードの選択"画面が開くので"Pygame Zero"を選択する
- 以下のコードを記述する
```python
WIDTH = 800
HEIGHT = 600
TITILE = "Hello World!"

def draw():
    screen.fill((128, 0, 0))
```
- "プレイ"ボタンを押す(セーブをしていなかったら、「名前をつけて保存」が表示される)
- 赤い画面が表示されたら成功！

<br></br>

### Pycharm 始め方

- **Pycharm Community Edition** を起動する
- **"Create New Project"**
- **"Location"** に保存したい場所とフォルダー名を設定 ex. "PC-16¥Desktop¥<好きな名前>"
- **"Project Interpreter"** をクリックする
- そうすると　**"Existing Interpreter"** と **"System Interpreter"**　が選択肢で表示される
- **"System Interpreter"** を選択し、"C¥Program - - - - - .python.exe" と書いてある右の下向き矢印をクリックするとその他のpythonへの選択肢がでる。
- 選択肢の中の **"C:¥ProgramData¥Anaconda3¥python.exe"** を選ぶ
- 左 **Pane** にある **"Project"** 以下にある自分で名付けたフォルダ名を選択し、画面上部の **「ファイル」** メニューから **"New"** を選択
- **"Python File"** を選択し、ファイル名を設定する



# Python 環境設定

## Mac編

* [Anaconda](https://www.anaconda.com/download/#macos)をインストール
  * Anacondaとは`Python`だけでなく、必要なライブラリなどを含めて全て入っている総合環境

### インストール終了後、確認
* Macの **Application** &rarr; **Utilities** の中にある **Terminal** を起動する
* `python` と入力
  * 出力は`Python3.7.0` `anaconda` ~~ となるはず

### Terminal の基本的な使い方
例: `/User/myname/code/Documents/practice.xlsx`
* `cd` (current directory)
  * 役割:   現在いるフォルダから違うフォルダに移動するためのcommand
  * 使い方: (`/code/`にいる場合)
    * `Documents`に移動する場合
      * `cd Documents`
    * `myname`フォルダに移動する場合
      * `cd ../`

* `idle`を起動する
  * コマンド:   `idle`

*






:imp: 始め方 :smiling_imp:

+ **Windowsメニュー** - **全てのプログラム** - **Anaconda** - **Anaconda Prompt** を開く

+ `python` と打ち(pythonソフトを起動)、`Python 3.7.0 (anaconda ~~ ` と出力されるのを確認する
+ `>>` という文字の横に `import pygame` と打ち、`pygame` がインストールされているかを確認する（エラーがでなければOK)
+ **Ctrl** + **D** を2回打てば、pythonソフトから抜けることができる
+ 抜け出たあと、 `idle`と打てばidleが起動する


 :smile: <b> VSCode編 </b> :smiley:

<p>

+ デスクトップに今日、使うフォルダを用意(日本語は使わない)
+ プログラムの中から **VSCode** を起動
+ **ファイル** &rarr; **フォルダを開く** &rarr; **[自分がデスクトップに作ったフォルダを選択]**
+ **ファイル** &rarr; **新規ファイル** で新しいファイルをフォルダに作成
#### プログラムの走らせ方
* **ターミナル** &rarr; **統合ターミナル** で画面したにターミナル画面が出る(Powershellのようなもの)
+ ターミナル画面の **powershell** を押す
 or
* **表示** &rarr; **New Terminal** で画面したにターミナル画面が出る(Powershellのようなもの)
+ `python main.py`と打つとプログラムが走る(`main.py`のファイル名は自分のつけたファイル名に変更)
+ ターミナル画面の **powershell** を押す

</p>

</details>

<br></br>

<details>

<summary>  :smile: <b> PyCharm編 </b> :smiley:  </summary>

<p>

+ デスクトップに今日、使うフォルダを用意(日本語は使わない)
+ プログラムの中から **PyCharm** を起動
+ **Create New Project** &rarr; **locationの中のパスの右にあるフォルダアイコンをクリックする** &rarr; **[自分がデスクトップに作ったフォルダを選択]**
+ [自分がデスクトップに作ったフォルダ]の選択し、**ファイル** &rarr; **新規ファイル** で新しいファイルをフォルダに作成

</p>

</details>

<br></br>
