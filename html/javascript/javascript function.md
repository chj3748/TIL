# function

##### 정의 및 형식

```javascript
// *이름이 없는 함수도 있음
function 함수이름(전달인자1, 전달인자2 [...]){
    함수 실행 코드;
    return 반환값; // 없을시 undefined 반환
}

// 함수 호출
var value = 함수이름(매개변수1, 매개변수2 [,...]); 
//반환값을 value에 할당
```

##### 특징

- 전달인자의 데이터 타입 제한 x
- 형 및 갯수 검사 x -> 프로그래밍의 유연함 증가
- 전달인자 생략 가능 -> 모자란 전달인자는 undefined처리

```javascript
function copyArray(arr, addEle){
    var tempArray = [];
    for(var i in arr)tempArray[i] = arr[i];
    if (addEle) tempArray.push(addEle);
    return tempArray;
}
var testArray = [1,2,3];
var a = copyArray(testArray); // 1,2,3
var b = copyArray(testArray,4); // 1,2,3,4
```

- 길이가 정해지지 않은 전달인자 사용가능
  - arguments : 전달인자를 의미하는 배열 형태의 객체

```javascript
function copyArray(arr, addEle){
    var tempArray = [];
    for(var i in arr)tempArray[i] = arr[i];
    //if (addEle) tempArray.push(addEle);
    // 0번째 값인 arr을 제외하기때문에 a=1부터 시작
    for (var a =1; a<arguments.length; a++){
        tempArray[tempArray.length]=arguments[a];
    }
    //
    return tempArray;
}
```

##### argument

- 활용하여 전달인자 개수 검사, 데이터 타입 검사 가능