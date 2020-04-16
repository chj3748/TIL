def rec(node): # value구하는 함수, 즉 tree[node]의 0번째 값을 구하는 함수
    if len(tree[node])==1: # 리프 노드일때
        return tree[node][0]
    elif len(tree[node])==2: # 자식노드가 1개일때
        return rec(tree[node][1])
    elif len(tree[node]) == 3: # 자식노드가 2개일때
        return rec(tree[node][1])+rec(tree[node][2])


T=int(input())
for t in range(1,T+1):
    n, m, l = map(int,input().split())
    tree=[[0] for _ in range(n+1)]
    for i in range(m):
        node, val = map(int,input().split())
        tree[node][0]=val
    # print(tree)

    for i in range(1,n-m+1):
        if i*2<=n:
            tree[i].append(i*2)
        if (i*2)+1<=n:
            tree[i].append((i*2)+1)
    # print(tree)

    result = rec(l)
    print('#{} {}'.format(t,result))