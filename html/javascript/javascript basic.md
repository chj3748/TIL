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



##### 단순 데이터 타입

- null 
  - 0 , ""와는 다름
  - 어떤 데이터 타입도 가지고 있지 않음
  - 변수에 아무 값이 담겨 있지 않음
- undefine
  - 정의되어 있지 않음
  - 값이 할당된 적 없는 변수, 생성되지 않는 객체에 접근할 때
  - null과 구분이 쉽지 않음



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

