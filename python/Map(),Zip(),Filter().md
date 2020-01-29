# Map(),Zip(),Filter()

- #### map(function, iterable) : 

  - Iterable의 모든 요소에 function을 적용한 후 그 결과 반환
  - 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range
  - return은 `map_object` 형태

```python
numbers = [1, 2, 3]
# 위의 코드를 문자열 '123'으로 만드세요
#list comprehension을 사용할때
result = [str(number) for number in numbers]
print(''.join(result))

#map 사용할때
result = map(str,numbers)
print(''.join(result))
```

```python
numbers = ['1', '2', '3']
# 위의 코드를 숫자열 '123'으로 만드세요
#list comprehension을 사용할때
result = [int(number) for number in numbers]
print(100*result[0]+10*result[1]+result[2])

#map 사용할때
result= list(map(int,numbers))
print(100*result[0]+10*result[1]+result[2])
```

```python
#일반형
text = input('데이터를 입력해주세요 : ')
slice_result=text.split(" ")
result=list(map(int,slice_result))
print(result)

#축약형
result=list(map(int,input('데이터를 입력해주세요 : ').split(" ")))
print(result)
```

```python
# 세제곱의 결과를 나타내는 함수
def cube(n):
    return n**3
numbers =[1,2,3]
print(list(map(cube,numbers)))
```

- #### `zip(*iterables)` : 

  - 복수의 iterable 객체를 모아줌
  - 결과는 튜플의 모음으로 구성된 `zip object` 를 반환

```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']
# 한 명씩 순서대로 매칭시켜봅시다.
# 예) {'jane': 'justin', 'iu': 'david', 'mary': 'kim'}
{girl:boy for girl,boy in zip(girls,boys)}
```
  - - zip은 반드시 길이가 같을 때 사용해야함. 다르다면 가장 짧은 것을 기준으로 구성

    ```python
    girls = ['jane', 'iu', 'mary']
    boys = ['justin', 'david']
    {girl:boy for girl,boy in zip(girls,boys)}
    ```

    - 길이가 긴 것을 맞춰서 할 수도 있지만, 사용할 일이 없음

    ```python
    from itertools import zip_longest
    list(zip_longest(girls,boys, fillvalue='짝이없습니다.'))
    ```



- #### `filter(function, iterable)` : 

  - iterable에서 function의 반환된 결과가 `True` 인 것들만 구성하여 반환
  - `filter object` 를 반환

```python
# 홀수인지 판단하는 코드를 작성하세요.
def odd(num):
    if num%2:
        return True
    else:
        return False
    #나머지가 1=> 홀수=> True
    #나머지가 0=> 짝수=> False
#    return num%2
numbers = [1,2,3,4,5,6,7,8,9,10]
result = list(filter(odd,numbers))
print(result)

# 다음의 list comprehension과 동일하다.
[num for num in numbers if odd(num)]
[num for num in numbers if num %2 ==1]
```

