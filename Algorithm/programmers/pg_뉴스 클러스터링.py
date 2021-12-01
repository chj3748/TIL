# string | programmers 뉴스 클러스터링
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(str1, str2):
    from collections import defaultdict
    str1 = str1.lower()
    str2 = str2.lower()
    set1 = defaultdict(int)
    set2 = defaultdict(int)

    set1_total = 0
    for i in range(len(str1) - 1):
        temp = str1[i: i + 2]
        if temp.isalpha():
            set1[temp] += 1
            set1_total += 1

    set2_total = 0
    for i in range(len(str2) - 1):
        temp = str2[i: i + 2]
        if temp.isalpha():
            set2[temp] += 1
            set2_total += 1

    inter_cnt = 0
    for k in set2.keys():
        if set1[k]:
            inter_cnt += min(set1[k], set2[k])
    total_cnt = set1_total + set2_total - inter_cnt
    return int(inter_cnt / total_cnt * 65536) if total_cnt else 65536