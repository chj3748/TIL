# 배열

##### 생성

1. 리터럴을 사용한 생성

```javascript
// 비어있는 배열, 생성 후 원소 추가 가능
var emptyArray = [];
// 기존 원소 + 특정 원소 추가, 수정, 삭제 가능
var oddNumber =[1,3,5,7,9];
// 원소는 어떤 데이터 타입도 가능
var testArray = [1, "two", {three:3}, [4,5], function(){ return "six"}, 3+4 , true];
```

2. 생성자를 사용한 생성

```javascript
// 빈 배열 생성
var emptyArray = new Array();
// 원소지정 생성
var oddNumber = new Array(1,3,5,7,9);
// 배열 길이 할당
var fixedEmpty = new Array(10);
```

##### 특징

1. 배열 크기 지정 필요 x
2. 배열의 인덱스는 0이상의 정수
   - 그렇지 않을 경우는 property를 생성하게 됨
3. 배열은 참조 타입
   - 새로운 변수에 단순할당으로는 복사x
   - 이름만 바뀌거나 추가될뿐
   - 진짜 복사를 하려면 함수를 사용해야함 
4. 배열이 생성되면 Array객체의 인스턴스이고 length 프로퍼티를 가짐
   - 배열이 아닌 일반 객체이면 length프로퍼티가 없음

##### 원소 순회 및 접근

- 순회

  1. for/in 문:

     ```javascript
     var numberString = ["one", "two", "three", "four", "five"];
     // a는 배열 모든 원소의 인덱스 차례로 순환
     for (var a in numberString){
         document.writeln("<p>" + numberString[a] + "</p>");
     }
     ```

  2. length 메소드를 이용한 순환문

     ```javascript
     var numberString = ["one", "two", "three", "four", "five"];
     for (var i=0; i<numberString.length; i++){
         document.writeln("<p>" + numberString[i] + "</p>");
     }
     ```

- 배열의 원소 추가/ 수정

  ```javascript
  // 3번째 인덱스의 원소가 있다면 값이 수정
  testArray[3]="test";
  // 없다면 추가
  // 원소 추가는 마지막 원소의 인덱스를 알아야 추가 가능
  // 모를때는 배열 길이를 알아낸 뒤 추가
  testArray[testArray.length] = 6;
  ```

- 배열의 원소 삭제

  ```javascript
  delete testArray[4];
  ```

  

##### 메소드

- sort()
  - 배열 자체를 정렬
  - 문자 정렬 방식 ( 23 이 4보다 앞에 정렬됨 )
  - 숫자도 문자로 인식하여 정렬
- reverse()
  - sort()와는 반대로 정렬
- concat()
  - 배열 연결
  - 전달 인자 : 추가할 배열
  - 새로운 배열 반환
- slice()
  - 배열의 일부분 반환
  - 전달 인자 : 배열의 시작[, 끝]
  - 새로운 배열 반환
- splice()
  - 배열의 일부분 삭제 삽입 등 여러 작업 가능
  - 전달 인자 : start[, deleteCount[, item1[, item2[, ...]]]])
  - start : 배열의 변경을 시작할 인덱스
  - deleteCount : 배열에서 제거할 요소의 수입니다.
  - item : 배열에 추가할 요소, 지정x-> 제거만 함
- push()
  - 배열의 마지막에 원소 추가
  - 반환값 : 새로운 배열 길이 반환
- pop()
  - 배열의 마지막 원소 제거
  - 반환값 : 제거된 원소 반환
- unshift()
  - 배열의 맨 앞에 원소 추가
  - 반환값 : 새로운 배열 길이 반환
- shift()
  - 배열의 맨 앞의 원소 제거
  - 반환값 : 제거된 원소 반환