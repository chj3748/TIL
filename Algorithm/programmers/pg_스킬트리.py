# deque | programmers 스킬트리
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        checking = list(skill)
        for s in skill_tree:
            if s in checking:
                if s != checking.pop(0):
                    break
        else:
            answer += 1
    return answer