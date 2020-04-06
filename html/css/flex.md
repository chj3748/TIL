# flex

- `flex` 이전에는 배치를 위해서 float, position 지정을 해야했음

#### flex 주요 개념

- container, item

```html
<style>
	.container{
    display: flex;
    }
</style>
<div class="container">
    <div class="item"></div>
    <div class="item"></div>
</div>
```

- main axis, cross axis
- flex 정의시
  - main axis을 기준을 ㅗ배치가 시작된다(기본은 row)
    - 먼역, row-reverse로 지정하게 된다면, 오른쪽 끝부터 배치가 시작됨
  - 모든 item은 cross axis을 모두 채운다
    - align-item 기본값이 stretch로 설정되어있기때문
  - 모든 item은 본인의 너비 혹은 컨텐츠 영역만큼 너비를 가진다.
    - 경우에 따라서, 본인이 지정받은 너비보다 적을 수 있다.(`flex-wrap : nowrap`이 기본값이기 때문)
      - 전체 아이템의 너비의 합이 컨테이너의 너비보다 작을때

##### flex 속성

###### 1. flex-grow



###### 2. justify-content

###### 3. align-item