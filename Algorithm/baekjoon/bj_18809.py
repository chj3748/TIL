# Gaaaaaaaaaaaaaarden
def select_soil(k, now, soil_idx):
    if k == G + R:
        g_r_combi(soil_idx, 0, 0, [])
    else:
        for s in range(now, S):
            select_soil(k+1, s+1, soil_idx + [s])


def g_r_combi(soil_idx, k, now, temp):
    if k == G:
        g, r = [], []
        for i in range(G+R):
            if i in temp:
                g.append(soil[soil_idx[i]])
            else:
                r.append(soil[soil_idx[i]])
        solve(g, r)
    else:
        for s in range(now, G+R):
            g_r_combi(soil_idx, k+1, s+1, temp + [s])


def solve(g, r):
    global max_flower
    flower = 0
    # 0: 호수, 1, 2: 퍼질 수 있는 땅, 3: green, 4: red
    copy = [land[n][:] for n in range(N)]
    for (n, m) in g:
        copy[n][m] = 3
    for (n, m) in r:
        copy[n][m] = 4
    while True:
        if not g or not r:
            break
        tmp_green = []
        while g:
            n, m = g.pop(0)
            # 녹색 배양액을 뿌렸었는데 꽃이 된 곳은 지나침
            if copy[n][m] == 0: continue
            copy[n][m] = 0
            for nn, nm in (0, -1), (0, 1), (1, 0), (-1, 0):
                vn, vm = n + nn, m+nm
                if not (0 <= vn < N and 0 <= vm < M): continue
                if copy[vn][vm] == 1 or copy[vn][vm] == 2:
                    tmp_green.append((vn, vm))
                    copy[vn][vm] = 3
        g = tmp_green

        tmp_red = []
        while r:
            n, m = r.pop(0)
            copy[n][m] = 0
            for nn, nm in (0, -1), (0, 1), (1, 0), (-1, 0):
                vn, vm = n + nn, m + nm
                if not (0 <= vn < N and 0 <= vm < M): continue
                if copy[vn][vm] == 1 or copy[vn][vm] == 2:
                    tmp_red.append((vn, vm))
                    copy[vn][vm] = 4
                elif copy[vn][vm] == 3:
                    copy[vn][vm] = 0
                    flower += 1
        r = tmp_red

    max_flower = max(flower, max_flower)


N, M, G, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]
soil = []

# 배양액 뿌릴 수 있는 땅
for n in range(N):
    for m in range(M):
        if land[n][m] == 2:
            soil.append((n, m))

S = len(soil)
max_flower = 0
select_soil(0, 0, [])

print(max_flower)