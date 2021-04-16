# Theory_String

#### ASCII

- 문자의 표현은 1967년 미국에서 제정한 ASCII라는 문자 인코딩 표준을 사용한다.
- 아스키는 7bit인코딩으로 128문자를 표현함
  - 33개의 출력 불가능한 제어문자
  - 95개의 출력 가능한 문자

#### 유니코드

- 국가간의 정보를 주고받을때 자국의 코드체계를 타국가가 가지고 있지않으면 잘못된 해석 가능

- 다국어 처리를 위해 마련한 표준을 유니코드라고 함

  - 유니코드 인코딩

    UTF-8		web

    UTF-16	windows,java

    UTF-32	unix

#### 패턴매칭

- 고지식한 패턴 검색 알고리즘(Brute Force)

```python
#1
p = 'mor'
txt ='good morning'
n=len(p)
m=len(txt)
for i in range(m):
    for j in range(n):
        if txt[i+j]==p[j]:
            pass
        else:
            break
    else:
        print(1)
        break
else:
    print(-1)
#2    
def find():
    for i in  range(0,len(str2)-len(str1)+1):
        j=0
        while str1[j] == str2[i+j]:
            j+=1
            if j == len(str1):
                return i
    return -1
str1 = 'mor'
str2 = 'good morning'
r = find()
print('패턴의 위치 : {}'.format(r))
#3
t=input()
p=input()
lenp=len(p)
lent=len(t)
for i in range(lent-lenp+1):
    if p[0:lenp]==t[i:i+lenp]:
        res=1
        break
    else:
        res=0
print(res)
```

- 카프-라빈 알고리즘
- KMP 알고리즘
- 보이어-무어 알고리즘



#### 문자열의 암호화

- 시저 암호
- 단일 치환 암호
- bit열의 암호화 (XOR연산)
- 