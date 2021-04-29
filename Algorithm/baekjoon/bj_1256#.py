# 수학 dp 조합 | bj 1256 사전
import sys
import itertools
import math

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

N, M, K = map(int, inp().split())
check = [0] * (N + M)
if K > math.factorial(N + M) / (math.factorial(N) * math.factorial(M)):
    print(-1)
    sys.exit(0)

# 시간 초과 => dp로 설계해야함
# def combi(cnt, a_cnt, z_cnt, sequence):
#     global total
#     if cnt == N + M:
#         total += 1
#         if total == K:
#             print(sequence)
#             sys.exit(0)
#         return
#     if a_cnt < N:
#         combi(cnt + 1, a_cnt + 1, z_cnt, sequence + 'a')
#     if z_cnt < M:
#         combi(cnt + 1, a_cnt, z_cnt + 1, sequence + 'z')
#
#
# total = 0
#
# combi(0, 0, 0, '')

answer = ''
while N + M != 0:  # a와 z를 다 소모할때까지
    if N > 0:  # 단 a가 한개라도 남아있을때 다음에 올 문자가 a라고 가정
        # 다음에 올 문자가 a라는 가정하에 나오는 경우의 수
        combi_cnt = math.factorial(N - 1 + M) / (math.factorial(N - 1) * math.factorial(M))
        if K <= combi_cnt: # 만약 찾아야하는 문자가 a를 선두로 하고 가능하면 a를 추가
            answer += 'a'
            N -= 1
        else:  # 불가능하다면 선두문자는 z이고 k = a선두일때 + 찾아야하는 순서 가 된다
            # 즉 z가 선두일때 찾아야하는 new_k = k - combi_cnt 이다
            answer += 'z'
            K -= combi_cnt
            M -= 1
    else:  # a가 남아있지않다면 어쩌피 남은 문자는 모두 z
        answer += 'z'
        M -= 1

print(answer)
