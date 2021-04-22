# bf 그리디 | bj 1339 단어 수학
import sys

inp = sys.stdin.readline

#  알파벳 -> 숫자 단, 중복 없이
                        # 사실상 의미없음
alpha_dict = {}  # char : [최대포지션, 가중치]  =>> char : 가중치
words = []
N = int(inp())
for _ in range(N):
    word = list(inp().strip())[::-1]  # 숫자가 작은것부터 뽑도록 역순으로 뽑음
    for idx, char in enumerate(word):
        # if alpha_dict.get(char):
        #     if alpha_dict[char][0] < idx:
        #         alpha_dict[char] = [idx, alpha_dict[char][1] + 10 ** idx]
        #     else:
        #         alpha_dict[char] = [alpha_dict[char][0], alpha_dict[char][1] + 10 ** idx]
        # else:
        #     alpha_dict[char] = [idx, 10 ** idx]

        # 최대포지션이 가중치때문에 의미가 없어져서 바꾼 코드
        if alpha_dict.get(char):    # 이미 존재하면 추가적으로 가중치만 합
            alpha_dict[char] = alpha_dict[char] + 10 ** idx
        else:   # 처음이면 가중치 입력
            alpha_dict[char] = 10 ** idx
    words.append(word)

# 가중치가 큰 순으로 정렬
sorted_dic = sorted(alpha_dict.items(), key=lambda x: (x[1]), reverse=True)

# 가중치가 높은것부터 9~0 숫자 할당
number = 9
for data in sorted_dic:
    alpha_dict[data[0]] = number
    number -= 1

total = 0
for word in words:
    temp = 0
    for idx, char in enumerate(word):
        temp += alpha_dict[char] * (10 ** idx)
    total += temp

print(total)
