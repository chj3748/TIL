def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    words = [begin]+words
    length = len(words)
    arr = [ [0 for i in range(length)] for j in range(length)]
    for first in range(length-1):
        for second in range(first+1, length):
            cnt=0
            for idx in range(len(begin)):
                if words[first][idx]!=words[second][idx]:
                    cnt+=1
            if cnt==1:
                arr[first][second]=1
                arr[second][first]=1
    targeti=words.index(target)
    stack=[[0]]
    visit=[0]
    while stack:
        p=stack.pop(0)
        temp=[]
        answer+=1
        for next in p:
            visit.append(next)
            for f in range(len(arr[next])):
                if arr[next][f]==1:
                    if f == targeti:
                        return answer
                    if f not in visit:
                        temp.append(f)
        stack.append(temp)