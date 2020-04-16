T= int(input())
for t in range(1,T+1):
    e, n = map(int,input().split())
    tree=[ [] for _ in range(e+2)]
    cnt=0
    link=list(map(int,input().split()))
    for i in range(e):
        tree[link[2*i]].append(link[(2*i)+1])
    # print(tree)
    queue=[n]
    while queue:
        cnt += 1
        node = queue.pop()
        if tree[node] is not None:
            queue.extend(tree[node])

    print('#{} {}'.format(t,cnt))