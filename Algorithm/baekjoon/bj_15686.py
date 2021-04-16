import itertools


def bfs(home):
    d=999
    for place in chickenset:
        temp= abs(place[0]-home[0])+abs(place[1]-home[1])
        d= min(d,temp)
    return d


n,m = map(int,input().split())
arr = [ list(map(int,input().split())) for _ in range(n)]
chicken = []
homes=[]
for i in range(n):
    for j in range(n):
        v = arr[i][j]
        if v ==2:
           chicken.append((i,j))
        elif v == 1:
            homes.append((i,j))
powersets = list(itertools.combinations(chicken, m))

min_d = 9999
for chickenset in powersets:
    total_d=0
    for home in homes:
        if total_d >= min_d:
            break
        total_d+= bfs(home)
    min_d= min(total_d, min_d)
print(min_d)