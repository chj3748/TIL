# 링크드리스트 힙? | programmers 표편집
# github.com/chj3748
import sys

def input():
    return sys.stdin.readline().rstrip()


def solution(n, k, cmd):
    default = [1] * n
    ht = [[i - 1, i + 1] for i in range(n)]
    ht[0][0] = 0
    ht[n - 1][1] = n - 1
    delete_list = []
    end = n - 1  # 제일 끝 수
    for c in cmd:
        c = c.split()
        if len(c) == 1:
            if c[0] == 'C':  # 삭제
                delete_list.append(k)
                default[k] = 0
                head, tale = ht[k]
                ht[head][1] = tale
                ht[tale][0] = head

                if k == end:
                    k = ht[k][0]
                    end = k
                else:
                    k = ht[k][1]

            else:  # 롤백
                r_k = delete_list.pop()
                default[r_k] = 1
                if r_k > end:
                    end = r_k
                head, tale = ht[r_k]
                if r_k == 0:
                    pass
                else:
                    ht[head][1] = r_k
                if r_k == n - 1:
                    pass
                else:
                    ht[tale][0] = r_k

        else:
            if c[0] == 'U':  # 위로 이동
                for _ in range(int(c[1])):
                    k = ht[k][0]
            else:  # 아래로 이동
                for _ in range(int(c[1])):
                    k = ht[k][1]
    answer = ['X'] * n
    for idx in range(n):
        if default[idx] == 1:
            answer[idx] = 'O'
    return ''.join(answer)