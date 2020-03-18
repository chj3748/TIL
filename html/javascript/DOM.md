# DOM

- 웹 브라우저에 관련된 javascript
- 클라이언트 측 javascript의 핵심
- 웹 브라우저와 웹 문서의 내용을 객체화
  - 각각의 객체는 프로퍼티로 정보를 읽거나 설정 가능



##### windoww 객체

- 창의 크기
  - ui요소 포함
    - window.outerWidth
    - window.outerHeight
  - ui요소 미포함
    - window.innerWidth
    - window.innerHeight
- 창의 위치
  - 좌측상단부터 브라우저까지의 거리
    - window.screenX
    - window.screenY
- 창 내부 스크롤 조작
  - 이동거리 파악
    - window.pageXoffset
    - window.pageYoffset



- 윈도우를 생성하는 방법

```javascript
// 생성된 윈도우 객체 반환
var newWindow = window.open("login/index.html", "login",...)
                            
newWindow.close()
```





##### getElementsByTagName()

- 태그 네임으로 요소 선택

##### getElementById()

- id 속성 값으로 노드 선택
- id속성은 유일한 값으로 하나의 노드만 반환
- 특정 요소를 바로 선택하는 매우 강력한 프로퍼티

##### childNodes[]

- 노드 객체의 자식 노드 목록을 배열로 반환
- firstChild, lastChild : 첫번째, 마지막 노드 객체 반환

##### parendNode

- 부모 노드에 접근

##### nextSibling / preciousSibling

- nextSibling : 형제 계층의 바로 다음 노드에 접근
- previousSibling : 바로 앞 노드에 접근

##### getElementsByClassName()

- 요소의 class속성 값을 이용하여 노드 객체들을 배열로 반환

##### querySelectorAll()

- css셀렉터를 이용하여 일치하는 노드 객체들을 배열로 반환





#### document

##### write

- 문서 내에 콘텐츠를 추가하는 메소드
- 함수 내부에 사용하여 이벤트로 사용을하면 기존 문서 삭제후 새로운 내용 입력

##### createElement()

- 요소 생성

##### createTextNode()

- 텍스트 노드 생성

##### appendChild()

- 특정 노드에 자식노드를 삽입

##### insertBefore()

- 특정 요소 앞에 삽입하기 위해 사용
- 부모노드.insertBefore(삽입할 노드, 레퍼런스 노드)

##### replaceChild

- 자식 노드 중 특정 노드를 새로운 노드로 치환
- 부모노드.replaceChild(새로운 노드, 바뀔 노드)



#### 노드 속성 조작

##### getAttribute()

- 노드의 속성값을 가져온다
- 노드.getAttribute("속성명")

##### setAttribute()

- 노드의 속성을 속성값으로 설정한다.

- 노드.setAttribute("속성명", "속성값")



#### CSS속성 적용

- 노드.style.css속성 = css속성값
- 단 `-`은 모두 대문자로 바꿔서 입력해야함



#### innerHtml

- createElement() 와 createTextNode() 그리고 appendChild()를 한꺼번에 처리하는 효과 발휘