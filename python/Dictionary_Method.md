# Dictionary_Method

#### 추가 및 삭제

- `.pop(key[, default])` : key가 딕셔너리에 있으면 제거하고 그 값을 반환, 그렇지 않으면 default를 반환
  - default가 없는 상태에서 딕셔너리에 없으면 `KeyError`가 발생
  - 두번째 인자로 default를 설정함으로써 에러발생 방지

```python
my_dict = {'apple': '사과', 'banana': '바나나'}
my_dict.pop('apple')
print(my_dict)
my_dict.pop('melon', 0)
```

- `.update()` : 값을 제공하는 key, value로 덮어씀
- key가 없으면 새로 값 추가

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
my_dict.update(apple = '사과야아앙아아아아')
print(my_dict)
my_dict.update(grape = '포도야아앙아아아아')
print(my_dict)
```

- `.get(key[, default])` :  key를 통해 value를 가져옴

  - 절대로 `KeyError`가 발생하지 않는다. default는 기본적으로 `None`임

```python
my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
print(my_dict.get('apple'))
print(my_dict.get('pineapple'))
print(my_dict.get('pineapple','키가 없어요'))
```

#### Dictionary comprehension

![image-20200128160022222](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200128160022222.png)

```python
#예제 1
## 세제곱 딕셔너리 생성하기
cubic_number= {i:i**3 for i in range(1,11)}
cubic_number
```

```python
#예제 2
## 미세먼지 농도 80초과 뽑기
dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45, '중국': 200}
over_dust = { key:value for key,value in dusts.items() if value>80}
print(over_dust)
```

```python
#예제 3
##미세먼지 농도가 80초과는 나쁨 80이하는 보통으로 하는 value를 가지도록 바꾸세요.
over_dust = { key:'나쁨' if value>80 else'보통' for key,value in dusts.items() }
print(over_dust)
```

```python
#예제4
##80초과 나쁨 50초과 보통 50미만 좋음
over_dust = { key:'나쁨' if value>80 else '보통' if value>50 else '좋음' for key,value in dusts.items() }
print(over_dust)
```

