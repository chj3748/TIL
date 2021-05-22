# 그리디 | bj 13019 A를 B로
import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

string1 = input()
string2 = input()

change = 0

pointer1 = pointer2 = len(string1) - 1
s1_dict = defaultdict(int)
s2_dict = defaultdict(int)
while pointer1 >= 0 and pointer2 >= 0:
    p1_s = string1[pointer1]
    p2_s = string2[pointer2]
    if p1_s == p2_s:
        pointer2 -= 1
    else:
        change += 1
        s1_dict[string1[pointer1]] += 1
    pointer1 -= 1
while pointer2 >= 0:
    s2_dict[string2[pointer2]] += 1
    pointer2 -= 1

if s1_dict == s2_dict:
    print(change)
else:
    print(-1)


