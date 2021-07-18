# 문자열 | bj 4446 ROT13
# github.com/chj3748
import sys

#
# def input():
#     return sys.stdin.readline()

vowels = 'aiyeou'
consonants = 'bkxznhdcwgpvjqtsrlmf'
decoding_key = {}
for idx, val in enumerate(vowels):
    decoding_key[val] = [idx, 0]
    decoding_key[val.upper()] = [idx, 1]
for idx, val in enumerate(consonants):
    decoding_key[val] = [idx, 2]
    decoding_key[val.upper()] = [idx, 3]

len_c = len(consonants)
len_v = len(vowels)
while True:
    try:
        string = input()
        answer = []
        for s in string:
            if s.isalpha():
                i, list_n = decoding_key[s]
                if list_n == 0:
                    i = (len_v + i - 3) % len_v
                    dec_s = vowels[i]
                elif list_n == 1:
                    i = (len_v + i - 3) % len_v
                    dec_s = vowels[i].upper()
                elif list_n == 2:
                    i = (len_c + i - 10) % len_c
                    dec_s = consonants[i]
                elif list_n == 3:
                    i = (len_c + i - 10) % len_c
                    dec_s = consonants[i].upper()
                answer.append(dec_s)
            else:
                answer.append(s)
        print(''.join(answer))
    except EOFError:
        break