# 구현 시뮬레이션 | bj 1713 후보 추천하기
import sys

inp = sys.stdin.readline

N = int(inp())
total_student = int(inp())
student_select = list(map(int, inp().split()))

# [학생번호, 추천수, 후보등록날짜]
candidates = []
for order, student in enumerate(student_select):
    candidates.sort(key=lambda x: (x[1], x[2]))
    # 첫 등록
    if order == 0:
        candidates.append([student, 0, order])
    else:
        # 학생이 이미 등록된경우
        for idx, candidate in enumerate(list(map(list, zip(*candidates)))[0]):
            if student == candidate:
                candidates[idx][1] += 1
                break
        else:
            # 등록안된경우
            # 사진틀이 없는경우
            if len(candidates) == N:
                candidates[0] = [student, 0, order]
            else:
                # 사진틀 여분이 있는 경우
                candidates.append([student, 0, order])
candidates.sort(key=lambda x: x[0])
print(*list(map(list, zip(*candidates)))[0])
