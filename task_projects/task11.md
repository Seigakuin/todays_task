# Task11
### テーマ： Dictionary

* 以下にあるのは、あるクラスの点数です。
1. 以下のDictionary から、Tom の点数だけを表示しなさい。
2. `for`ループを使って、一人ひとりの点数を表示しなさい。
3. `for`ループを使って、クラスの平均を出しなさい。
4. 以下のような結果が出るようにしなさい。


* ３つ目の題は`enumerate()`を使う

使用例
```python
my_list = {'a': 1, 'b': 2, 'c': 3}

for key, value in enumerate(my_list):
    print(key, value)

```
出力

```python
0 a
1 b
2 c
```


#### スタートコード (これはコピペしても良い)    *  **???** の箇所を自分のコードに置き換えること
```python
my_class = {
  "Tom": 95,
  "Garnet": 76,
  "Jason": 69
 }

print("Tomの点数だけを出力")
print(???)

print("3人の点数を出力")
for ???:
    print(???)
    
print("3人の点数を文字列と共に出力")
for ???, ??? in enumerate(???):
    print(??? + "'s score is " + str(???))




```

#### 出力
```python
Tomの点数だけを出力
95
3人の点数を出力
95
76
69
3人の点数を文字列と共に出力
Tom's score is 99
Garnet's score is 76
Jason's score is 69

```


[back home](https://github.com/Seigakuin/todays_task)
