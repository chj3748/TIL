# swea 5207 이진탐색
def binsearch(num,e):
    start=0
    end=e
    mid = (start + end) // 2
    if num == dictionary[mid]:
        return True
    elif num < dictionary[mid]:
        choice='left'
        end = mid - 1
    else:
        choice = 'right'
        start = mid + 1
    while(start <= end):
        mid = (start+end)//2
        if num == dictionary[mid]:
            return True
        elif num < dictionary[mid]:
            next_choice='left'
            end = mid - 1
        else:
            next_choice='right'
            start = mid + 1
        if choice == next_choice:
            return False
        choice = next_choice
    return False


T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    dictionary = list(map(int,input().split()))
    find_list = list(map(int,input().split()))
    dictionary.sort()
    global result
    result = 0
    for find in find_list:
        if binsearch(find,len(dictionary)-1):
            result+=1

    print('#{} {}'.format(t, result))