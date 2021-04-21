# bf 백트래킹 dfs? 비트마스킹 | bj 1062 가르침
import sys
inp = sys.stdin.readline


def dfs(idx, cnt, learned):
    global max_read
    if cnt == K - 5:
        temp_cnt = 0
        for word in words:
            for c_word in word:
                if c_word not in learned:
                    break
            else:
                temp_cnt += 1
        if temp_cnt > max_read:
            max_read = temp_cnt
    else:
        # 시간단축의 핵심부분.
        # 앞에서부터 학습/미학습을 하고 가기 때문에
        # 다음학습때 이전학습 문자를 고려할 필요없음
        for i in range(idx, len(check_list)):
            to_learn = check_list[i]
            unicode = ord(to_learn) - ord('a')
            if char_list[unicode] == -1:
                char_list[unicode] = 1
                dfs(i, cnt + 1, learned + [to_learn])
                char_list[unicode] = -1


N, K = map(int, inp().split())
basic = ['a', 'n', 't', 'i', 'c']
words = []
check_list = set()
# 입력받은 문자열중 basic을 제외하고 학습이 필요한 문자열을 중복없이 저장
for _ in range(N):
    temp = set()
    for char in inp().strip():
        if char not in basic:
            temp.add(char)
            if char not in check_list:
                check_list.add(char)
    words.append(list(temp))
# 학습 유무를 판단할 리스트
char_list = [0] * 26
for check_char in check_list:
    # 학습이 필요한 문자는 -1, 필요없는 문자는 0, 학습한 문자는 1
    char_list[ord(check_char) - ord('a')] = -1

max_read = 0

if K < 5: # 학습가능한 횟수 < 필수 학습 횟수
    print(max_read)
elif len(check_list) + 5 <= K: # 학습이 필요한 문자 <= 학습가능 횟수
    print(N)
else: # 몇몇 문자만 학습가능한 경우
    check_list=list(check_list)
    dfs(0, 0, [])
    print(max_read)