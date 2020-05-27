# 5201 컨테이너 운송
for t in range(1,int(input())+1):
    N, M = map(int,input().split())
    containers=list(map(int,input().split()))
    trucks = list(map(int,input().split()))

    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    result=0
    for truck in trucks:
        for container in containers:
            if container<= truck:
                result+=container
                containers.remove(container)
                break
    print('#{} {}'.format(t,result))