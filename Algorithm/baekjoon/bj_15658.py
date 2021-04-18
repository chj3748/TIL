# 백트래킹 브루트포스 구현 문자열 | bj 15658 연산자 끼워넣기(2)
N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))
max_ = -10 ** 9
min_ = 10 ** 9

def dfs(idx, num, add, sub, mul, div):
    global max_, min_
    print(N, idx, num, add,sub,mul, div)
    if idx == N:
        max_ = max(max_, num)
        min_ = min(min_, num)
        return
    else:
        if add>0:
            dfs(idx + 1, num + numbers[idx], add - 1, sub, mul, div)
        if sub>0:
            dfs(idx + 1, num - numbers[idx], add, sub - 1, mul, div)
        if mul>0:
            dfs(idx + 1, num * numbers[idx], add, sub, mul - 1, div)
        if div>0:
            if num >= 0:
                dfs(idx + 1, num // numbers[idx], add, sub, mul, div - 1)
            else:
                dfs(idx + 1, (abs(num)// numbers[idx] )* (-1), add, sub, mul, div - 1)


dfs(1, numbers[0], add, sub, mul, div)
print(max_)
print(min_)