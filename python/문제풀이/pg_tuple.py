def solution(s):
    numlist=s.replace('{', '').replace('}', '')
    numdic={}
    for number in map(int,numlist.split(',')):
        numdic[number]=numdic.get(number,0)+1
    answer = [0]*len(numdic)
    for key, val in numdic.items():
        answer[-val]=key
    return answer