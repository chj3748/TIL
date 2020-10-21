# swea dp 완전탐색 | 1486 장훈이의 높은 선반
# 방법 1
# import itertools
# T=int(input())
# for t in range(1,T+1):
#     n,h=map(int,input().split())
#     members=list(map(int,input().split()))
#     powerset=[]
#     for r in range(1,n+1):
#         powerset.extend(list(itertools.combinations(members,r)))
#     resulth=sum(members)
#     for i in powerset:
#         if sum(i)>=h:
#             if sum(i)<resulth:
#                 resulth=sum(i)
#     print('#{} {}'.format(t,resulth-h))


# 방법2
def find_height(idx, temp_height):
    global result
    if temp_height >= result:
        return
    if B <= temp_height < result:
        result = temp_height
        return
    else:
        for i in range(idx, N):
            if used[i] == 0:
                used[i] = 1
                find_height(i, temp_height + people[i])
                used[i] = 0
    return


T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    people = list(map(int, input().split()))
    used = [0] * N
    result = float('inf')
    find_height(0, 0)

    print('#{} {}'.format(t, result - B))
