# sort | programmers 가장 큰 수
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(numbers):
    if len(numbers) == numbers.count(0):
        return '0'
    from functools import cmp_to_key

    def comparator(x, y):
        if int(x + y) < int(y + x):
            return 1
        else:
            return -1
        return 0

    return ''.join(sorted(map(str, numbers), key=cmp_to_key(comparator)))

# max_size = 4
# def f1(x):
#     temp = x[:]
#     while len(temp) < max_size:
#         if temp[-1] == '0':
#             temp += '1'
#         else :temp+=temp[0]
#     return temp

# def solution(numbers):
#     if len(numbers) == numbers.count(0):
#         return '0'
#     answer = ""
#     split_numbers = map(list, map(str,numbers))

#     sorted_numbers = sorted(split_numbers,key=f1,reverse=True)
#     i = 0
#     while i < len(sorted_numbers)-1:
#         a = str("".join(sorted_numbers[i]))
#         b = str("".join(sorted_numbers[i+1]))
#         if int(b+a) > int (a+b):
#             sorted_numbers[i],sorted_numbers[i+1] = sorted_numbers[i+1],sorted_numbers[i]
#             i -= 1
#             if i < 0:
#                 i = 0
#             continue
#         i += 1
#     for number in sorted_numbers:
#         answer += "".join(number)
#     return answer