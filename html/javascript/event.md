# event

웹 브라우저에서 웹 문서에 특별한 일이 있을때 발생하는 신호

- 이벤트 핸들러 : DOM객체에 할당되어 해당 객체의 이벤트 반응에 호출되어 처리되는 프로퍼티
  - 이벤트 발생 감지
  - 이벤트 감지
  - 지정된 코드 또는 함수 호출



| 종류           | 역할                                                |
| -------------- | --------------------------------------------------- |
| onclick        | 마우스 클릭                                         |
| onmousedown    | 마우스 단추 눌림                                    |
| onmouseup      | 눌렸던 마우스 단추가 올려졌는지                     |
| onmouseover    | 마우스 커서가 특정 객체 위에 올라갔는지             |
| onmouseout     | 마우스 커서가 특정 객체에서 벗어났는지              |
| onmousemove    | 마우스 커서의 이동                                  |
|                |                                                     |
| onload         | 로딩 완료                                           |
| onunload       | 현재 화면에서 벗어날때<br />링크로 페이지 이동 등등 |
|                |                                                     |
| onsubmit       | 서식이 전송됨                                       |
| onreset        | 서식이 재설정됨                                     |
| onfocus        | 특정 서식 요소에 커서가 접근함                      |
| onblur         | 커서가 벗어남                                       |
|                |                                                     |
| onkeydown      | 키보드가 눌렸는지                                   |
| onkeypress     | 키보드가 눌려지고 있는지                            |
| onkeyup        | 키보드가 올려졌는지                                 |
|                |                                                     |
| onbeforeonload | 도큐먼트 로딩전에                                   |
| onhaschange    | 도큐먼트에 변화가 있을때                            |
| oninput        | 서식에 사용자입력이 있을때                          |
| onmousewheel   | 마우스 휠을 돌릴때                                  |

#### 이벤트 핸들러 사용방법

1. 객체에 직접 속성 형태로 적용
2. javascript에 이벤트 핸들러 적용

- 이벤트 핸들러에 기본적으로 true값이 리턴
- 만약 false값이 리턴되면 기본 이벤트 기능 수행 x



##### addEventListener

- 형식
  - addEventListener(이벤트핸들러, 실행 될 함수 , 이벤트 감지)
- preventDefault() : 기본 이벤트 기능 막기



##### this / target

- target사용이 이벤트 전파시 발생하는 문제를 피할 수 있음



##### removeEventListener

- addEventListener와 똑같은 3개의 인수 필요