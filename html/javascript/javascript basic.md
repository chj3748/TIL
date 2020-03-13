# javascript basic

javascript : 문서의 기능 정의

##### 특징

- 스크립트 언어

  - 인터프리터를 통해 바로 실행
  - 데이터 타입, 형 변환 수월
  - 속도가 느림
  - 실행 환경 제한
  - 텍스트 에디터와 웹 브라우저 만 있으면 프로그래밍 가능
  - 코드 테스트가 수월

- 함수형 언어 : 함수를 기본으로 하는 방식

  - 선언적 프로그래밍
    - html 요소 동적으로 처리 가능
  - 1급 함수 : 함수 자체를 데이터로 활용 가능
  - 변수의 유효 범위 = 함수의 유효 범위

- 대소문자 구분

  - but! HTML에서는 대소문자 구분 x 

- 자유로운 변수

  - 선언되지 않은 변수에 값 할당 : 자동 변수 생성
  - 선언 되지 않은 변수 사용 -> 에러

- 참조 변수 가능

  

##### 단순 데이터 타입

- null 
  - 0 , ""와는 다름
  - 어떤 데이터 타입도 가지고 있지 않음
  - 변수에 아무 값이 담겨 있지 않음
- undefine
  - 정의되어 있지 않음
  - 값이 할당된 적 없는 변수, 생성되지 않는 객체에 접근할 때
  - null과 구분이 쉽지 않음

##### 객체

```javascript
var obj= new Object();
/*새로운 비어있는 객체 생성*/
obj.width = 300;
//property 설정하기

//미리 정의되어 있는 새로운 data객체 생성
var now = new Date();
```

##### 배열

```javascript
var a = new Array();
a[0]=10;
a[1]=true;
a[2]=3.5
a[3]="orange"

var a = {10,true,3.5, "orange"};
```

##### 함수

```javascript
function toCelsius (fahr){
    var celsius = 5*(fahr -32)/9;
    return celsius;
}
var temp = toCelsius(40);

//함수 리터럴 : 함수를 값으로 변수에 할당 대부분의 함수는 이름이 없음
var toCelsius = function(fahr){
    var celsius = 5*(fahr -32)/9;
    return celsius;
};
var temp = toCelsius(40);
```



##### 변수의 유효 범위

- 지역변수
  - 함수 안에 선언된 변수
  - 함수 내부로 사용 제한 

```javascript
testScope1();
function testScope1(){
    var scope = "local_A";
    document.writeln(scope);
    testScope2();
    
    function testScope2(){
        document.writeln(scope);
        var scope = "local_B"
        document.writeln(scope);
    }
}
// 결과는 local_A undefined local_B 이다
// testscope2의 중간에서 변수 선언이 이뤄졌지만 그것은 함수 전체에 영향을 가함
```

- 전역변수
  - 가능한 최소한의 전역변수를 사용하는것을 권장



##### javascript의 상수

- Number.MAX_VALUE : 표현가능한 최대 수
- Number.MIN_VALUE : 표현가능한 최소 수
- INFINITY : 무한대를 의미
- Number.POSITIVE_INFINITY : MAX_VALUE보다 큰 양의 무한대
- Number.NAGATIVE_INFINITY : MIN_VALUE보다 작은 음의 무한대
- Number.MAX_VALUE : 숫자가 아닌 값
- Number.NaN : 숫자가 아닌 값



##### escape sequence

​	: 문자열로 사용 시 잘못 해석되어 사용이 불가능하거나 보이지 않는 기능 문자 표시

| properties | description                        |
| ---------- | ---------------------------------- |
| \b         | backspace                          |
| \f         | form feed                          |
| \n         | newline                            |
| \O         | Nul character                      |
| \r         | carriage return                    |
| \t         | horizontal tab                     |
| \v         | vertical tab                       |
| \\' or \\" | (single/double)quote or apostrophe |
| \\\        | backslash                          |

