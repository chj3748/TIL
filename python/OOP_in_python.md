# OOP_in_python

####		: (Object-Oriented Programming)

객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것

- #### 클래스(Class)

  - 객체를 표현하는 문법
  - 같은 종류(또는 문제 해결을 위한)의 집단에 속하는 **속성(attribute)**과 **행위(behavior)**를 정의한 것으로 객체지향 프로그램의 기본적인 사용자 정의 데이터형(user define data type)이라고 할 수 있음
  - 클래스는 프로그래머가 아니지만 해결해야 할 문제가 속하는 영역에 종사하는 사람이라면 사용할 수 있고, 다른 클래스 또는 외부 요소와 독립적으로 디자인

- #### 인스턴스(instance)

  - 클래스의 인스턴스/객체(실제로 메모리상에 할당된 것)

  - 객체는 자신 고유의 속성(attribute)을 가지며 클래스에서 정의한 행위(behavior)를 수행할 수 있다.

  - 객체의 행위는 클래스에 정의된 행위에 대한 정의(메서드)를 공유함으로써 메모리를 경제적으로 사용

    

    - 인스턴스와 객체는 같은 것을 의미한다.
    - 보통 객체만 지칭할 때는 단순히 객체(object)라고 부른다.
    - 하지만 클래스와 연관지어서 말할 때는 인스턴스(instance)라고 부른다.




- #### 속성(attribute)

  - 클래스/인스턴스 가 가지고 있는 속성(값)

- #### 메서드(Method)

  - 클래스/인스턴스 가 할 수 있는 행위(함수)
  - dir을 사용하면 사용가능한 메소드 목록을 확인가능



#### Class생성

```python
### pascal case로 클래스명 작성
class User:
    name = '홍길동'
    
```

- python 출력의 비밀?? : str 과 repr

  ```python
  class User:
      name = '홍길동'
      username = 'default'
      password = ''
  
      def __str__(self):
          return 'print 안에 넣으면 이렇게 나오고'
      def __repr__(self):
          return '그냥 객체만 놔두면 이게 나오지요'
  ```



<example>

`MyList` 클래스가 가지는 변수와 메서드는 아래와 같습니다.

```
* 멤버 변수(클래스 변수)
data : 비어 있는 리스트

* 메서드
append() : 값을 받아 data 에 추가합니다. 리턴 값은 없습니다.
pop() : 마지막에 있는 값을 삭제하고, 해당 값을 리턴합니다.
reverse() : 제자리에서 뒤집고 리턴 값은 없습니다.
count() : data 리스트 요소의 개수를 리턴합니다.
clear() : 값을 모두 삭제합니다. 리턴값은 없습니다.

__repr__ : ex) '내 리스트에는 [1, 2, 3] 이 담겨있다.'
```

```python
class MyList:
    data=[]
    def append(self,d):
        self.data.append(d)
    def pop(self):
        return self.data.pop()
    def reverse(self):
        self.data.reverse()
    def count(self,a):
        return self.data.count(a)
    def clear(self):
        self.data.clear()
    def __repr__(self):
        return '내 리스트에는 {}이 담겨있다'.format(self.data)
```



#### 생성자/소멸자

- 생성자
  - 인스턴스 객체가 생성될 때 호출되는 함수.
  - 인스턴스가 생성될 때 인스턴스의 속성을 정의할 수 있다.

- 소멸자
  - 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 함수.

```python
def __init__(self):
    print('생성될 때 자동으로 호출되는 메서드입니다.')

def __del__(self):
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
```

위의 형식처럼 양쪽에 언더스코어가 있는 메서드는 특별한 일을 하기 위해 만들어진 메서드이기 때문에 `스페셜 메서드` 혹은 `매직 메서드`라고 불립니다.

- 매직(스페셜) 메서드 형태: `__someting__`



