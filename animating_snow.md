# :computer: 聖学院プログラミング部 :computer:

:cat: <b> Arcade Project - Animating Snow </b> :mouse:

- ### [Arcade - Animating Snow 1](https://github.com/Seigakuin/todays_task/blob/master/py_arcade/animating_snow_folder/animating_snow_1.py)

  - Goal:

    - 一粒の Snow を降らせる

  - Exercises:
    - 雪の場所、大きさを変えてみよう

* ### [Arcade - Animating Snow 2](https://github.com/Seigakuin/todays_task/blob/master/py_arcade/animating_snow_folder/animating_snow_2.py)

  - Goal:

    - 雪の粒のステータスを入れておく Dictionary を作り、それで呼び出す

  - Exercises:
    - circle ではなく、別の形を使ってみよう。

- ### [Arcade - Animating Snow 3](https://github.com/Seigakuin/todays_task/blob/master/py_arcade/animating_snow_folder/animating_snow_3.py)

  - Goal:

    - 雪の粒をたくさん作る(for ループを使用)

  - Exercises:
    - 雪の粒の数を変更する

* ### [Arcade - Animating Snow 4](https://github.com/Seigakuin/todays_task/blob/master/py_arcade/animating_snow_folder/animating_snow_4.py)

  - Goal:

    - 雪の粒を降らせる(下に移動)

  - Exercises:
    - 降るスピードを変更する
    - (Difficult)各雪の粒のステータスに"speed"を加え、雪の粒それぞれにスピードをつける

- ### [Arcade - Animating Snow 5](https://github.com/Seigakuin/todays_task/blob/master/py_arcade/animating_snow_folder/animating_snow_5.py)

  - Goal:

    - 雪の粒が画面下の外に移動したら、再び上に戻す(if を使用)

  - Exercises:
    - 雪の粒が突然上に移動してしまうエラーを直す
    - 同じ縦に位置から降り始めるので、それを random にする

- ### [Arcade - Animating Snow 6](https://github.com/Seigakuin/todays_task/blob/master/py_arcade/animating_snow_folder/animating_snow_6.py)

  - Goal:

    - Snow クラスを作成し、Snow クラスのインスタンスでステータスを管理する

  - Exercises:
    - Snow インスタンスの数に変化をつけよう(動きが鈍くなるはず！)
    - これを解決するためには根本的になにかを変えないといけない

* ### [Arcade - Animating Snow 7](https://github.com/Seigakuin/todays_task/blob/master/py_arcade/animating_snow_folder/animating_snow_7.py)

  - Goal:

    - arcade.Sprite クラスから Snow クラスを継承しよう
      - こうすることにより各インスタンスが管理しやすくなる
      - 動きも良くなる

  - Exercises:
    - インスタンスの数を限界まで増やしてみよう
    - (Difficult) Snow クラスの update に新たなルールをつけてみよう
      - ex. center_x のスタート位置を変える
      - ex. 再描画するときに radius に変化をつける

* ### [Arcade - Animating Snow 8](https://github.com/Seigakuin/todays_task/blob/master/py_arcade/animating_snow_folder/animating_snow_8.py)

  - Goal:

    - `on_key_press()`を使い、下キーを押した時に雪を増やす
    - MyGame クラスに`add_snow()`メソッド(関数)を加える

  - Exercises:
    - `add_snow()`を改良し、一度に増やす数を増やす
      - ヒント： `add_snow()`の中に for ループを入れる

* ### [Arcade - Animating Snow 9](https://github.com/Seigakuin/todays_task/blob/master/py_arcade/animating_snow_folder/animating_snow_9.py)

  - Goal:

    - Box クラスを新たに作成
      - 機能： 衝突した Snow を消す
    - all_list を作成
      - all_list は SpriteList のインスタンス
      - Box のインスタンスとすべての Snow インスタンスを入れておく SpriteList
        理由： Box, Snow すべてを一気に update(), draw()を呼び出すため
    - MyGame クラスの update()に
      - arcade.check_for_collision_with_list()を使い、衝突判定をし、衝突した Snow インスタンスをリストに格納
      - remove_from_sprite_lists() 衝突した Snow インスタンスを snow_list から取り除く

  - Exercises:
    - Box クラスの`update`メソッドを改良し、動きを工夫する

- ### [Arcade - Animating Snow 10](https://github.com/Seigakuin/todays_task/blob/master/py_arcade/animating_snow_folder/animating_snow_10.py)

  - Goal:

    - キーに合わせて Box を動かす

  - Exercises:
    - 衝突判定を工夫する
      - ex. 衝突した雪のスピードを下げる
