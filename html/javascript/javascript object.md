# object

##### 정의

- 여러 값을 모아 놓은 데이터 타입

##### 생성

- 일반적인 객체지향에서는 class의 instance로 생성

- javascript에는 class가 없음

  1. 객체 literal을 이용

  2. new 연산자 이용(생성자 함수 사용)

     ```javascript
     function square(w,h){
         this.width = w;
         this.height = h;
         this.faceColor ="yellow";
         this.position = {x:100,y:100};
     }
     var mysquare = new square( 20,30);
     ```

##### property

- 객체를 표현하는 변수
- 어떠한 데이터 타입이라도 가능
- `.`을 이용해서 접근
- delete연산자를 이용해서 프로퍼티 삭제 가능

##### method

- 함수로 이루어진 property

```javascript
var square = {
    // property
    width :50, 
    height: 100, 
    faceColor: "yello", 
    borderColor : "black",
    //method
    area : function(){ return this.width * this.height;}
}
// 호출
square.area()
```



#### 내장 객체

- javascript에서 제공하는 유용한 객체

1. number object

   - 숫자에 대응하는 객체 타입
   - 생성자를 사용하여 생성 가능

   ```javascript
   var numberObject = new Number(1000);
   // 1000이라는 숫자 객체 생성
   
   var n = 1000;
   var s = n.toString();
   // 일시적으로 n이 number객체가 되어서 메소드를 실행하고 다시 숫자타입으로 돌아옴
   ```

   - toString : 현재 객체의 값을 문자로 변환
   - toFixed : 특정 갯수의 소수점 아래 자리수를 보이게 문자로 변환
   - toExponential :  소수점 이상의 하나의 자리와 지정한 숫자 만큼의 소수점 이하 자리수를 유지한채 지수 표기한 후 문자로 변환
   - toPrecision : 일정한 유효숫자를 유지한 후 문자로 변환

2. string object

   - 문자열에 대응하는 객체 타입
   - indexOf : 일치하는 첫문자의 위치를 반환
   - lastIndexOf : 일치하는 마지막 문자의 위치를 반환
   - substr : 메소드 인자로 문자의시작 위치와 길이를 전달 -> 해당 문자열 반환
   - slice : substr과 비슷, 메소드 인자로 문자시작위치와 끝위치를 전달 -> 해당 문자열 반환
   - concat : 문자열 연결
   - split : 메소드인자를 기준으로 문자를 분할 후 배열로 반환

3. math object

   - round : 메소드 인자값의 소수점 이하 자리의 반올림값을 반환
   - ceil : 올림
   - floor : 버림
   - abs : 절대값
   - pow : 멱승
   - min/max : 최소/최대값 반환
   - random : 0~1사이의 무작위 난수 발생