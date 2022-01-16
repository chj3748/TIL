# hash | programmers 신고 결과 받기
# github.com/chj3748
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    user_idxs = defaultdict(int)
    for user_idx, user_id in enumerate(id_list):
        user_idxs[user_id] = user_idx

    reports = defaultdict(set)
    for r in report:
        reporter, target = r.split()
        reports[target].add(user_idxs[reporter])

    for reporters in reports.values():
        if len(reporters) >= k:
            for reporter in reporters:
                answer[reporter] += 1

    return answer