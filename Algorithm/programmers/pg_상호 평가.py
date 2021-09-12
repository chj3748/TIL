# math | programmers 상호 평가
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


from collections import defaultdict


def find_grade(score):
    grade = ['F', 'F', 'F', 'F', 'F', 'D', 'D', 'C', 'B', 'A', 'A']
    return grade[int(score // 10)]
    # return 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 50 else 'F'


def solution(scores):
    def cal_average(idx):
        get_score = defaultdict(int)
        for j in range(len(scores)):
            get_score[scores[j][idx]] += 1
        max_score = max(get_score.keys())
        min_score = min(get_score.keys())
        my_score = scores[idx][idx]
        total_people = len(scores)
        total_score = sum([key * val for key, val in get_score.items()])
        if my_score == max_score or my_score == min_score:
            if get_score[my_score] == 1:
                total_people -= 1
                total_score -= my_score

        return find_grade(total_score / total_people)

    return ''.join([cal_average(i) for i in range(len(scores))])