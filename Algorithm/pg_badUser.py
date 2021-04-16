def sublist(answer,ban_list,temp,idx):
    if idx==len(temp):
        if not answer:
            answer.append(set(temp))
        else:
            # print(33, answer,temp)
            if set(temp) not in answer:
                # print(2222222, set(temp))
                answer.append(set(temp))
        return

    for ban in ban_list[idx]:
        if ban not in temp:
            temp[idx]=ban
            sublist(answer,ban_list,temp,idx+1)
            temp[idx]=0


def solution(user_id, banned_id):
    ban_list=[ [] for _ in range(len(banned_id))]
    for user in user_id:
        for b in range(len(banned_id)):
            if len(user)== len(banned_id[b]):
                for i in range(len(user)):
                    if banned_id[b][i]=='*' or user[i]==banned_id[b][i]:
                        pass
                    else:
                        break
                else:
                    ban_list[b].append(user)
    li=[0]*len(ban_list)
    idx=0
    answer=[]
    # print(ban_list)
    sublist(answer,ban_list,li,0)
    cnt=len(answer)

    return cnt