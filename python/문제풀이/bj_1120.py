a,b= input().split()
result= 999
def check(f,s):
    cnt=0
    for i in range(len(f)):
        if f[i]=='?' or f[i]==s[i]:
            pass
        else:
            cnt+=1
    return cnt

def addchar(word1, word2,head,tail):
    used.append([head,tail])
    global result
    if len(word1)==len(word2):
        result= min(result, check(word1,word2))
        return
    else:
        if [head+1,tail] not in used:
            addchar('?'+word1,word2,head+1,tail)
        if [head,tail+1] not in used:
            addchar(word1+'?',word2,head,tail+1)
used=[]
addchar(a,b,0,0)

print(result)


#
# def check(f,s,idx):
#     cnt=0
#     for i in range(len(f)):
#         if f[i]==s[i+idx]:
#             pass
#         else:
#             cnt+=1
#     return cnt
#
# def addchar(word1, word2, start,end):
#     global result
#     if len(word1)+start+end == len(word2):
#         result= min(result, check(word1,word2,start))
#         return
#     else:
#         addchar(word1,word2,start+1,end)
#         addchar(word1,word2,start, end+1)
#
# addchar(a,b,0,0)