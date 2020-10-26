# swea dp bfs dfs | 1248 공통조상
def find_ancestor(son,check):
    global result
    q =[]
    q.append(son)
    while q:
        node = q.pop()
        if tree[node][1]:
            Next = tree[node][1][0]
            q.append(Next)
            if not check:
                ancestor.append(Next)
            else:
                if Next in ancestor:
                    result[0] = Next
                    return


def cal_subtree(start):
    global result
    cnt = 0
    q =[]
    q.append(start)
    while q:
        node = q.pop()
        cnt+=1
        if tree[node][0]:
            Next = tree[node][0]
            q.extend(Next)

    result[1]= cnt


T = int(input())
for t in range(1, T+1):
    V, E, son1, son2 = map(int, input().split())
    tree = {(i+1): [[],[]] for i in range(V)}
    edge = list(map(int,input().split()))
    for i in range(E):
        p, s = edge[2*i], edge[2*i+1]
        tree[p][0].append(s)
        tree[s][1].append(p)

    ancestor = []
    result = [1,V]
    find_ancestor(son1,False)
    find_ancestor(son2, True)

    cal_subtree(result[0])
    print('#{} {} {}'.format(t, result[0], result[1]))



