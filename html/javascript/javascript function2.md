# javascript function2

##### 생성자로 정의하기

```javascript
var 변수 = new Function(["전달인자1","전달인자2"],"함수코드");
// 전달인자는 생략가능, 변수임에도 불구하고 ""로 표기
```

- 필요한 기능 동적으로 생성
- 이름 없는 함수 생성

- 반복문에서 사용시 매번 함수를 동적으로 생성 하고 소멸시킴
  - 비효율적, 좋지 않은 결과 초래 가능

- 함수의 이름도 사실은 함수를 담는 변수
  - 함수 객체를 가리키는 참조

##### 함수 리터럴

```javascript
var toCelsius = function(faht){
    return Math.floor(5*(fahr-32)/9);
};
var value = toCelsius(100);
// 한번 사용되고 버려지는 형태로 사용
```

#### 배열 테스트 함수 (call-back 함수)

메소드 실행 시 자동으로 호출되는 함수

- Filter
- forEach
- every
- map
- some

###### 어휘적 유효 범위

- 함수가 실행될 떄 환영 유효 범위에 포함
- 함수가 정의 될 당시의 환경도 유효 범위도 포함

#### Closure

내부 함수를 리턴하는 중첩 함수

```javascript
function closureFunc(argA){
    return function(argB){
        return argA + argB;
    }
}
var temp = closureFunc(100);
// 위의 temp 는 아래와 같음
/*
argA = 100;
var temp = function(argB){
	return argA + argB;
}
*/
temp(50); // 150반환
```

- 클로저가 중요한 이유 : 

  - closureFunc이 실행되고 내부 함수 temp 반환 후 종료

  - 함수 종료시 가비지 콜렉션에 의해 객체 제거

    ** 종료된 함수 내부 변수 참조 가능

  