# Theory2

#### 2차원 배열

- 1차원 배열을 묶어놓은 배열
- 2차원 이상의 다차원 배열은 차원에 따라 index 선언

![image-20200203104841932](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200203104841932.png)



#### 비트연산자

![image-20200203164120941](Theory2.assets/image-20200203164120941.png)

- 예시) 간결하게 부분집합을 생성하는 방법

```python
arr =[3,6,7]#,1,5,4]
n=len(arr)
for i in range(1<<n):
    sub=[]
    for j in range(n):
        if i& (1<<j):
            sub.append(arr[j])
    print(sub)
```

