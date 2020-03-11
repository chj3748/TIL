# css expression2

1. 서체의 지정과 텍스트 설정

   - 이유: 문서 외형 꾸미기, 문서의 특성 제시, 구조 이해 도움
   - font-family : 비슷한 모양의 서체를 묶어서 제시
     - 형식 : font-family : (사용할 서체), (대안 서체1), (대안 서체 2);
     - serif : 명조체
     - sans-serif : 고딕체
     - monospace : 고정폭 글꼴
     - cursive : 필기체
     - fantasy : 그래픽과 같이 멋을 낸 서체
   - font-size : 크기 조절
     - 단위 : pt, pc, px, %, em, ex
   - font-style : 기울임
     - italic, oblique, normal
   - font-weight : 진하게
     - bold, bolder, lighter, 100~900, normal
   - font-variant : 텍스트 크기로 대소문자 표기
     - scall-cap
   - 텍스트 간격 설정
     - letter-spacing:  자간
     - word-spacing : 단어 간격
     - line-height : 행간
   - text-align : 정렬
     - 블록 레벨 요소에만 적용
     - left, right, center, justify, auto
     - 세로 정렬
       1. 인라인 : 상대적 수직위치
       2. 테이블 셀 : 상단 중단 하단 중 선택
   - text-indent : 들여쓰기

   

2. 컬러와 배경 설정하기

   - 16진수, 10진수, HSL, 색상 키워드 의 방법으로 가능

   - color : 색상 지정

   - background-color : 배경색 지정

   - background-image : 배경 이미지 설정

   - background-repeat : 반복 속성

     - repeat, repeat-x, repeat-y, no-repeat

   - background-attachment : 배경 이미지 고정

     - fixed, scroll

   - background-position : x, y 좌표 지정

   - background-size : 가로 세로 크기 지정(상대적 크기)

   - [그라디언트]: https://www.colorzilla.com/gradient-editor/

   

3. 목록 , 표꾸미기

   - 불릿 : 목록 아이템 앞에 붙은 숫자 혹은 특수문자
   - list-style-type : 불릿 지정
     - upper-alpha, lower-alpha, upper-roman, lower-roman
     - disc, circle, square
     - none
   - list-style-image : url을 이용해서 이미지 불릿 사용
   - list-style-position : 불릿 위치 지정
     - inside , outside
   - margin : 박스 형태 영역의 바깥쪽 여유공간
     - 셀에는 margin 설정 불가
   - padding : 박스 형태 영역의 안쪽 여유 공간
     - top right bottom left 순으로 지정 가능
   - border : 테두리
     - border-width, border-style, border-color
     - 위의 3개를 순서대로 축약형으로 표현 가능
     - border-style
       - none, hidden, solid, deshed, dotted, double, groove, ridge, inset, outset
     - 표의 각 셀마다 테두리를 표현하고 싶을시 tr td에 border속성 추가
     - border-spacing : 셀간격 설정
     - border-collapse : 간격 삭제
   - empty-cells : 비어있는 셀 감추기
     - hide, show
   - cation-side : 표의 제목 위치 설정
     - top, bottom

   

4. css 박스 모델

   - HTML 모든 요소가 사각형 영역을 가지고 있음
   - margin : 박스모델에서 border 바깥쪽 영역
     - 블록 레벨 요소는 상하좌우 적용
     - 인라인 레벨 요소는 좌우만 적용
     - margin 겹침 현상이 있음
   - padding : 박스모델에서 border 안쪽 영역
     - 블록 레벨 요소는 상하좌우 적용
     - 인라인 레벨 요소는 좌우만 적용
   - position : 다른 요소들과 어떤 관계 속에서 위치를 결정할지 설정
     - top, left, bottom, right로 포지션 설정
     - relative : 자신의 원래 위치에서 설정한 위치만큼 이동
     - absolute : 기본 흐름에서 벗어나 요소를 띄워 줌( 약간 공중에 뜬 느낌 레이아웃 영향을 받지않음)
       - z-index : 어떤 요소가 다른 요소위에 나타나는지 설정
       - 높게 설정 될수록 앞에 배치
       - 미설정시 요소가 나타난 순서대로 위에 제시
     - fixed : 부모 좌표를 넘어서 브라우저 원점에서 좌표를 정하게 되는 고정 위치



클리핑

- clip : 이미지 또는 요소의 특정 부분만 보이게 할때 사용
  - 요소의 포지션 속성은 absolute일때만 가능
  - rect(top좌표, right좌표, bottom좌표, left좌표)
  - top, bottom 좌표 각각은 요소 상단에서부터 시작
  - right, left 좌표 각각은 요소 좌측에서부터 시작

