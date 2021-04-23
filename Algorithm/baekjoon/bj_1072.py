# 수학 이분탐색? | bj 1072 게임
import sys

# sys.setrecursionlimit(10 ** 9)
inp = sys.stdin.readline

X, Y = map(int, inp().split())
Z = int(Y * 100 / X) # 나누기를 먼저하면 소수점자리수 표시문제로 인해 오답발생
if X == Y:
    print(-1)
    sys.exit(0)
if Z >= 99:
    print(-1)
    sys.exit(0)
# 시간 초과 코드
# cnt = 0
# while True:
#     cnt += 1
#     Y += 1
#     X += 1
#     new_Z = (Y / X) * 100
#     if int(new_Z) - int(Z) >= 1:
#         break
# print(cnt)

# 공식으로 푸는 방법
# (y + k)/(x + k)*100 - z >= 1
# (y+k)/(x+k) = (z+1)/100
# y+k = (z+1)/100 *(x+k)
# k -k(z+1)/100 = (z+1)/100 *(x) -y
# k = ((z+1)*(x) -100*y )/((100-(z+1)))
# k >= (xz + x - 100y) / (99-z)

K = (X * Z + X - 100 * Y) / (99 - Z)
if K % 1 == 0:
    K = int(K)
else:
    K = int(K) + 1
print(K)
