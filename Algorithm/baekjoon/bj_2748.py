# dp 수학 | bj 2748 피보나치 수2
import sys

# sys.setrecursionlimit(10 ** 9)
inp = sys.stdin.readline

n = int(inp())
fibo_memo = [-1] * (n + 1)
fibo_memo[0] = 0
fibo_memo[1] = 1


def fibo(find_n):
    if fibo_memo[find_n] != -1:
        return fibo_memo[find_n]
    else:
        fibo_memo[find_n] = fibo(find_n - 1) + fibo(find_n - 2)
        return fibo_memo[find_n]


fibo(n)
print(fibo_memo[n])
