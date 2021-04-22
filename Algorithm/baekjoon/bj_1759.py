# bj dp | 1759 암호만들기
# def secret_key(idx, cnt, key, vowel, consonant):
#     if cnt == L:
#         if vowel >= 1 and consonant >= 2:
#             print(key)
#             return
#     else:
#         if idx >= C:
#             return
#         if alpha[idx] in ['a', 'e', 'i', 'o', 'u']:
#             used[idx] = 1
#             secret_key(idx + 1, cnt + 1, key + alpha[idx], vowel + 1, consonant)
#             used[idx] = 0
#             secret_key(idx + 1, cnt, key, vowel, consonant)
#         else:
#             used[idx] = 1
#             secret_key(idx + 1, cnt + 1, key + alpha[idx], vowel, consonant + 1)
#             used[idx] = 0
#             secret_key(idx + 1, cnt, key, vowel, consonant)
#
#
# L, C = map(int, input().split())
# alpha = input().split()
# alpha.sort(key=lambda x: ord(x), reverse=False)
# used = [0] * C
# secret_key(0, 0, '', 0, 0)


# 2021.04.22풀이
import sys

inp = sys.stdin.readline


def make_secret_key(idx, cnt, vowel, consonant, string):
    if cnt == L:
        if vowel >= 1 and consonant >= 2:
            print(string)
        return
    if idx >= C:
        return
    if strings[idx] in ['a', 'e', 'i', 'o', 'u']:
        # 모음 사용
        make_secret_key(idx + 1, cnt + 1, vowel + 1, consonant, string + strings[idx])
    else:
        # 자음 사용
        make_secret_key(idx + 1, cnt + 1, vowel, consonant + 1, string + strings[idx])
    # 그냥 패스
    make_secret_key(idx + 1, cnt, vowel, consonant, string)


L, C = map(int, inp().split())
strings = inp().split()
strings.sort()  # strings.sort(key = lambda x : ord(x))
make_secret_key(0, 0, 0, 0, '')
