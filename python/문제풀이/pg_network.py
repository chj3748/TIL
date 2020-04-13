def solution(n, computers):
    visited=[0]*n
    stack=[]
    answer=0
    for computer in range(n):
        if visited[computer]==0:
            stack.append(computer)
            answer+=1
            while stack:
                cur=stack.pop()
                if visited[cur]==0:
                    visited[cur]=1
                    for next,val in enumerate(computers[cur]):
                        if val == 1:
                            stack.append(next)
    return answer