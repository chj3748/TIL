# dp dfs 트리 그래프 | bj 2533 사회망 서비스(SNS)
import sys

sys.setrecursionlimit(10 ** 9)
inp = sys.stdin.readline


def dfs(idx):
    visited[idx] = 1
    dp[idx] = [0, 1]
    for son in adjacency_list[idx]:
        if not visited[son]:  # 재방문 금지
            dfs(son)  # 루트 기준 리프 노드 까지 이동
            dp[idx][0] += dp[son][1]  # 현재위치가 ea가 아니면 자식은 무조건 ea이어야 함
            dp[idx][1] += min(dp[son])  # 현재위치가 ea이면 자식은 둘중 아무거나 되어도 됨


n = int(inp())
adjacency_list = [[] for _ in range(n + 1)]  # 인접 리스트
for _ in range(n - 1):
    u, v = map(int, inp().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

# dp[i]는 [i가 not ea일때 서브트리의 ea의 수, i가 ea일때 서브트리의 ea의 수]
# 즉 리프 노드일 경우 [0, 1]
dp = [[0, 0] for _ in range(n + 1)]
visited = [0] * (n + 1)
dfs(1)
print(min(dp[1]))  # 루트의 ea/not ea 각 경우 중 더 작은 값 뽑으면 됨
