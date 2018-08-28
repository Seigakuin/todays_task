# 課題  Level 19
## テーマ：Class 2

<br></br>
### 1
#### 課題： クラスにプロパティを与えよう
#### レベル： Easy 
<br></br>
### pseudo code (疑似コード)
1. `Animal` クラスに名前( `name` )と年齢 ( `age` )というプロパティを与え、名前に好きな名前、年齢を入力しなさい ( `__init__()` ファンクションが大事！！)
2. `Animal` クラスのインスタンスを変数 `myAnimal` を作成し、 2つのプロパティを表示しなさい

参考例
```python
class Person:
    def __init__(self):
        self.eye_color = "blue"
        self.gender = "Male"
    
    def sleep(self):
        printf("I'm sleeping...")

p = Person()
p.eye_color
p.gender
```
<br></br>
### 2
#### 課題： クラスに初期値を与えられるようにしよう
#### レベル： Easy 
<br></br>
### pseudo code (疑似コード)
1. 上記の`Animal`クラスを使う
2. `Animal` クラスを作成するときに `name` , `age` それぞれの初期値を与えられるようにしよう

<br></br>
実行例
```python
"""
>>> myAnimal = Animal("John", 45)
>>> myAnimal.name
John
>>> myAnimal.age
45

"""
```



<br></br>


[back home](https://github.com/Seigakuin/todays_task)