# String_Method

https://www.w3schools.com/python/python_ref_string.asp

#### 문자 변형

- `.capitalize()` : 앞글자를 대문자로 만들어 반환

- `.title()` : 어포스트로피(`'`)나 공백 이후를 대문자로 만들어 반환

- `.upper()` : 모두 대문자로 만들어 반환

- `lower()` : 모두 소문자로 만들어 반환

- `swapcase()` : 대 <-> 소문자로 변경하여 반환

- `.join(iterable)` :특정한 문자열로 만들어 반환. Iterable 을 separator 로 합쳐서 문자열로 반환

   > `iterable`
   	> 각각의 요소를 하나씩 반환할 수 있는 객체를 말한다. List와 Tuple, Dictionary와 Set 등이 여기에 속한다.

   ```python
   words = ['안녕', 'hello']
   " ".join(words)
   ```

- `.replace(old, new[, count])`

   > 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
   >
   > ```python
   > 'hello!!'.replace("l",'1')
   > ```
   >
   > count를 지정하면 해당 갯수만큼만 시행
   >
   > ```python
   > a= 'apple'
   > a.replace('p', '*', 1)
   > ```

- `.strip([chars])` : 특정한 문자들을 지정하여 제거 , 지정하지 않으면 공백 제거

   > 양쪽을 제거
   >
   > ```python
   > a= "          1234"
   > a.strip()
   > ```
   >
   > 왼쪽을 제거
   >
   > ```python
   > print('              1234            '.lstrip())
   > ```
   >
   > 오른쪽을 제거
   >
   > ```python
   > print('              1234            '.rstrip())
   > ```
   >
   > 특정문자 지정
   >
   > ```python
   > 'hihihihihihihihihihihihihihheheheheh'.strip('hi')
   > ```

#### 탐색 및 검증

- `.find(x [,start, end])` : x의 첫 번째 위치를 반환. 없으면 -1을 반환. 시작점과 끝점을 지정 가능

  ```python
  'apple'.find('p')
  ```

- `.index(x)` : x의 첫번째 위치를 반환합니다. 없으면, 오류가 발생

  ```PYTHON
  'apple'.index('l')
  'apple'.index('c')
  ```

- `.split()` : 문자열을 특정한 단위로 나누어 리스트로 반환

  ```python
  'a_b_c'.split('_')
  ```



#### 그 외 다양한 확인 메소드 : 참/거짓 반환

- `.isalpha()` : 영문자인지
- `.isdecimal()` : 십진숫자인지
- `.isdigit()` : 숫자인지
- `.isnumeric()` : 숫자형태인지
- `.isspace()` : 공백이있는지
- `.isupper()` : 대문자인지
- `.istitle()` : 대문자로 시작하는지
- `.islower()` : 소문자인지

