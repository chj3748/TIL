# MAX in SUM

다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

다음과 같은 5X5 배열에서 최댓값은 29이다.

![img](https://swexpertacademy.com/main/common/fileDownload.do?downloadType=CKEditorImages&fileId=AV2XTaX6DVkBBASl)


**[제약 사항]**

총 10개의 테스트 케이스가 주어진다.

배열의 크기는 100X100으로 동일하다.

각 행의 합은 integer 범위를 넘어가지 않는다.

동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
 
**[입력]**

각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.



#### 풀이

```python
def msum():
    qnumber= int(input())
    bg =[]
    sumli=[]
    vsumli=[0]*100
    crsum=0
    rcrsum=0
    for i in range(100):
        number= [int(x) for x in input().strip().split()]
        for j in range(100):
            vsumli[j]+=number[j]
        bg.append(number)
        sumli.append(sum(number))
        crsum+=bg[i][i]
        rcrsum+=bg[i][99-i]

    sumli.append(crsum)
    sumli.append(rcrsum)
    sumli+=vsumli

    return max(sumli)
for t in range(1,11):
    print(f'#{t} {msum()}')
```

