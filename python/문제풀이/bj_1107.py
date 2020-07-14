# bj dp | 1107 리모컨
def avail_number(num):
    i = 0
    if num == 0:
        return numbers[0]
    while pow(10,i) <= num :
        n = num%(int(pow(10,i+1)))
        n /= pow(10,i)
        if not numbers[int(n)]:
            return 0
        i+=1
    return i


numbers = [1]*10
N = int(input())
M = int(input())
if M > 0:
    for not_num in map(int,input().split()):
        numbers[not_num] = 0

minimum = abs(100-N)
for possible in range(0,1000001):
    a = avail_number(possible)
    if a != 0:
        if minimum > abs(possible-N)+a:
            minimum = abs(possible-N)+a
print(minimum)