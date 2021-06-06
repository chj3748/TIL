# 문자열 | bj 1718 암호
import sys


def input():
    return sys.stdin.readline().rstrip()


string = input()
secret_key = [ord(s_k) for s_k in input()]
answer = []
s_k_len = len(secret_key)
key_idx = 0
for s in string:
    if s == ' ':
        answer.append(' ')
    else:
        temp = ord(s) - secret_key[key_idx] + 96
        if temp <= 96:
            temp += 26
        answer.append(chr(temp))
    key_idx += 1
    if key_idx == s_k_len:
        key_idx %= s_k_len

print(''.join(answer))
