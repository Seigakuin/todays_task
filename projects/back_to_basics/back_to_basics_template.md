# ４択クイズを作ろう

## Level 3:

### 課題：


#### 条件：

#### ヒント：


#### 使用するデータ(コピペで良い)


#### ユーザーから見たプログラム

<details>

<summary> <b> Level 3 答え表示 </b> </summary>

<p>

```python

```

</p>
</details>

---




* dictionary の KeyとValueを取得するには...
* string(文字列)をつなげるには...
```python
d = {"key1": "value1", "key2": "value2", "key3": "value3"}

# dictionsryに.items()をつけることによって、
# dictionaryのkeyとvalueを同時に取得できる
for key, value in d.items():
    # stringは "+" でつなげることができる
    print(key + " - " + value)

```