# bj dp | 1759 암호만들기
def secret_key(idx, cnt, key, vowel, consonant):
    if cnt == L:
        if vowel >= 1 and consonant >= 2:
            print(key)
            return
    else:
        if idx >= C:
            return
        if alpha[idx] in ['a', 'e', 'i', 'o', 'u']:
            used[idx] = 1
            secret_key(idx + 1, cnt + 1, key + alpha[idx], vowel + 1, consonant)
            used[idx] = 0
            secret_key(idx + 1, cnt, key, vowel, consonant)
        else:
            used[idx] = 1
            secret_key(idx + 1, cnt + 1, key + alpha[idx], vowel, consonant + 1)
            used[idx] = 0
            secret_key(idx + 1, cnt, key, vowel, consonant)


L, C = map(int, input().split())
alpha = input().split()
alpha.sort(key=lambda x: ord(x), reverse=False)
used = [0] * C
secret_key(0, 0, '', 0, 0)
