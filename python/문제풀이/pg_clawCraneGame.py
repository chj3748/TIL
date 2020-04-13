def solution(board, moves):
    result=[]
    answer=0
    for move in moves:
        for row in range(len(board)):
            if board[row][move-1]!=0:
                temp=board[row][move-1]
                board[row][move-1]=0
                if len(result)>=1:
                    if result[-1]==temp:
                        result.pop()
                        answer+=2
                        break
                result.append(temp)
                break
    return answer