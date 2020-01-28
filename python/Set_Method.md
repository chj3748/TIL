# Set_Method

#### 추가 및 삭제

- `.add(elem)` : elem을 세트에 추가함

```python
a = {'사과', '바나나', '수박'}
a.add('포도')
print(a)
```

- `.update(*others)` : 여러가지의 값을 추가함
- 여기서 반드시 `iterable`한 값을 넣어야함

```python
a = {'사과', '바나나', '수박'}
a.update(['포도', '딸기'])
print(a)
```

- `.remove(elem)` : elem을 세트에서 삭제하고, 없으면 `KeyError`가 발생

```python
a = {'사과', '바나나', '수박'}
a.remove('사과')
print(a)
```

- `.discard(elem)` : x를 세트에서 삭제하고 없어도 에러가 발생하지 않음

```python
a = {'사과', '바나나', '수박'}
a.discard('포도')
print(a)
```

- `.pop()` : **`임의의 원소`**를 제거해 반환합니다.

```python
a = {'사과', '바나나', '수박', '아보카도'}
print(a.pop())
```



