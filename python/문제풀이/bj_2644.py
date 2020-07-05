# bj bfs | 2644 촌수계산
def cal_distance(n, p1,p2):
    q=[]
    q.append([p1,0])
    checked = [0]* (n+1)
    while q:
        person, cnt = q.pop(0)
        checked[person] = 1
        if person == p2:
            return cnt
        for next,val in enumerate(family[person]):
            if val != 0 and checked[next]==0:
                q.append([next,cnt+1])
    else:
        return -1



n = int(input())
p1, p2 =map(int, input().split())
m = int(input())
family = [ [0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    p , s = map(int,input().split())
    family[p][s]=1
    family[s][p]=-1

result = cal_distance(n, p1, p2)

print(result)
