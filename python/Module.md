# Module

#### 모듈

​	: 모듈은 파이썬 정의와 문장들을 담고 있는 파일

​	  파일의 이름은 모듈 이름에 확장자 `.py`를 붙임

|                        |                                                              |
| ---------------------- | ------------------------------------------------------------ |
| 모듈                   | 특정 기능을 .py 파일 단위로 작성한 것.                       |
| 패키지                 | 특정 기능과 관련된 여러 모듈들의 집합. 패키지 안에는 또다른 서브 패키지를 포함 할수도 있음. 보통 인터넷에 있는 패키지를 설치해서 사용 |
| 파이썬 표준 라이브러리 | 파이썬에 기본적으로 설치된 모듈과 내장 함수를 묶어서 파이썬 표준 라이브러리 (Python Standard Library, PSL) 라 함 |
| pip (패키지 관리자)    | `PyPI` 에 저장된 외부 패키지들을 설치하도록 도와줌           |

#### 모듈 생성

-  파일의 이름을 fibo.py 로 저장

```python
# fibo.py
def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)
    

def fibo_for(n):
    if n < 2: 
        return n
    
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b
```



#### 모듈 불러오기 : import

- 모듈을 활용하기 위해서는 반드시 `import`문을 통해 내장 모듈을 이름 공간으로 가져와야함

```python
import fibo
fibo.fibo_recursion(10)
fibo.fibo_for(10)
```

#### 패키지

- 패키지는 '점으로 구분된 모듈 이름' 을 써서 파이썬의 모듈 이름 공간을 구조화하는 방법
- 예를 들어, 모듈 이름 `myPackage.math`는 `myPackage`라는 이름의 패키지에 있는 `math`라는 이름의 서브 모듈을 가리킴
- 단, 파이썬이 디렉터리를 패키지로 취급하게 만들기 위해서 `__init__.py` 파일이 필요함
  - 이유는 string 처럼 흔히 쓰는 이름의 디렉터리가, 의도하지 않게 모듈 검색 경로의 뒤에 등장하는 올바른 모듈들을 가리는 일을 방지하기 위함

#### from - import -

- `from` *모듈명* `import` *어트리뷰트*

- `from` *모듈명* `import` `*`

- `from` *모듈명* `import` *어트리뷰트* `as`

```python
import module
import pakage1.module1, pakage2.module2
from module import var
from module import function
from module import Class
from module import *
from pakage.module import var, function, Class
```



#### 파이썬 기본 모듈 : [표준 라이브러리](https://docs.python.org/ko/3/library/index.html)에서 제공되는 모듈

- 수학 관련 함수(math)

  - 이외에도 분수(frctions), 십진(decimal), 통계(statistics)등이 있음

  - | 함수                | 비고                            |
      | ------------------- | ------------------------------- |
    | math.ceil(x)        | 소수점 올림                     |
    | math.floor(x)       | 소수점 내림                     |
    | math.trunc(x)       | 소수점 버림                     |
    | math.copysign(x, y) | y의 부호를 x에 적용한 값        |
    | math.fabs(x)        | float 절대값 - 복소수 오류 발생 |
    | math.factorial(x)   | 팩토리얼 계산 값                |
    | math.fmod(x, y)     | float 나머지 계산               |
    | math.fsum(iterable) | float 합                        |
    | math.modf(x)        | 소수부 정수부 분리              |
    |math.pow(x,y)|x의 y제곱의 결과|
  |math.sqrt(x)|x의 제곱근의 결과|
  |math.exp(x)|e^x 결과|
  |math.log(x[, base])|밑을 base로 하는 logx (base default 값은 e)|

- 난수 발생 관련 함수(random)
  - | 함수                   | 비고                        |
      | ---------------------- | --------------------------- |
    | random.sample(range,n) | 범위 사이의 n개 비복원 추출 |
    | random.random()        | 난수발생                    |
    | random.randint(x,y)    | x~y사이의 임의이 정수 반환  |
    | random.trunc(x)        | 소수점 버림                 |
    | random.shuffle(x)      | 시퀀스 x객체를 섞는다.      |

- 날짜 관련 모듈 : (datetime)
  
  - 날짜와 시간의 조합에 관련된 모듈
  
    - 어트리뷰트: year, month, day, hour, minute, second, microsecond 및 tzinfo.
  
  - | 함수                  | 비고                |
    | -------------------- | ------------------ |
    | datetime.now() | 오늘을 출력하는 함수 |
  | datetime.today() | 오늘을 출력하는 함수 |
    | datetime.utcnow() | UTC기준시도 출력 |
    | now.strftime('%Y %B %d') | 원하는 표기형식 지정 |
    | datetime(year, month, day, hour, minute, second, microsecond) | 특정한 날짜 |
    | timedelta(days=x) | 두 date, time 또는 datetime 인스턴스 간의 차이를 마이크로초 해상도로 나타내는 기간 |
    
  - | 형식 지시자(directive) | 의미                   |
    | ---------------------- | ---------------------- |
    | %y                     | 연도표기(00~99)        |
    | %Y                     | 연도표기(전체)         |
    | %b                     | 월 이름(축약)          |
    | %B                     | 월 이름(전체)          |
    | %m                     | 월 숫자(01~12)         |
    | %d                     | 일(01~31)              |
    | %H                     | 24시간 기준(00~23)     |
    | %I                     | 12시간 기준(01~12)     |
    | %M                     | 분(00~59)              |
    | %S                     | 초(00~61)              |
    | %p                     | 오전/오후              |
    | %a                     | 요일(축약)             |
    | %A                     | 요일(전체)             |
    | %w                     | 요일(숫자 : 일요일(0)) |
    | %j                     | 1월 1일부터 누적 날짜  |
  
  - | 속성/메소드 | 내용                 |
    | ----------- | -------------------- |
    | .year       | 년                   |
    | .month      | 월                   |
    | .day        | 일                   |
    | .hour       | 시                   |
    | .minute     | 분                   |
    | .second     | 초                   |
    | .weekday()  | 월요일을 0부터 6까지 |
  

