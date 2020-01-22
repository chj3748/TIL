# Function

#### ![function descrpition](https://user-images.githubusercontent.com/18046097/61181742-2984fd80-a665-11e9-9d5c-c90e8c64953e.png)

#### 함수의 선언

- 함수 선언은 `def`로 시작하여 `:`으로 끝나고, 다음은 `4spaces 들여쓰기`로 코드 블록을 만든다.

- 함수는 `매개변수(parameter)`를 넘겨줄 수도 있다.

- 함수는 동작후에 `return`을 통해 결과값을 전달 할 수도 있다. (`return` 값이 없으면, `None`을 반환한다.)

#### 함수의 호출

- 함수는 호출을 `func()` / `func(val1, val2)`와 같이 한다.

```python
#ex1
def func(parameter1, parameter2):
    code line1
    code line2
    return value
```

#### 함수의 `return`

- 함수는 반환되는 값이 있으며, 이는 어떠한 종류의 객체여도 상관없습니다.
- **한 개의 객체**만 반환됩니다.
- 함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아갑니다.

```python
#ex2
def my_list_max(l1, l2):
    if sum(l1)>sum(l2):
        return l1
    else:
        return l2
result = my_list_max([10, 3], [5, 9])
print(result)
```

#### 함수의 인자(argument)

1. ##### 위치 인자( Positional Arguments)

   - 함수는 기본적으로 인자를 위치로 판단합니다.

![function example 02](https://user-images.githubusercontent.com/18046097/61181743-2a1d9400-a665-11e9-8df2-e4856caf16e4.png)

2. ##### 기본 인자 값 (Default Argument Values)

   - 함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있습니다.
   - 기본 인자 값이 설정되어 있을 경우(기존 함수 호출과 동일)

   ![img](https://user-images.githubusercontent.com/18046097/61181744-2a1d9400-a665-11e9-9095-6924ca11122e.png)

   - 호출시 인자가 없을 경우(기본 인자 값이 활용)

   ![function example 03](https://user-images.githubusercontent.com/18046097/61181745-2a1d9400-a665-11e9-95ef-e50e463e1583.png)