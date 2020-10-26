# swea 완점탐색 dp | 1244 최대 상금
# def trade_number():
#     if num_li == max_num_li:
#         num_li[-1], num_li[-2] = num_li[-2], num_li[-1]
#     else:
#         h_idx = -1
#         b_idx = -1
#         for idx in range(trade):
#             if num_li[idx] != max_num_li[idx]:
#                 h_idx = idx
#                 break
#         max_temp=-1
#         for idx in range(trade - 1, -1, -1):
#             if num_li[idx] != max_num_li[idx]:
#                 if num_li[idx]>max_temp:
#                     max_temp=num_li[idx]
#                     b_idx = idx
#         if b_idx not in back_number:
#             if num_li[b_idx] != max_num_li[b_idx]:
#                 back_number.append(b_idx)
#         # print(h_idx,b_idx)
#         num_li[h_idx], num_li[b_idx] = num_li[b_idx], num_li[h_idx]
#         temp_used=[]
#         for idx in back_number:
#             temp_used.append(num_li[idx])
#         temp_used.sort(reverse=True)
#         back_number.sort()
#         print(temp_used,back_number)
#         for tidx,idx in enumerate(back_number):
#             num_li[idx]=temp_used[tidx]
# T = int(input())
# for t in range(1, T + 1):
#     numbers, trade = input().split()
#     num_li = list(map(int, numbers))
#     trade = int(trade)
#     max_num_li = sorted(num_li, reverse=True)
#     trade = len(num_li)
#     back_number=[]
#     # print('max:', max_num_li)
#     for i in range(trade):
#         trade_number()
#         print(num_li)
#
#     print('#{} {}'.format(t, ''.join(map(str,num_li))))
#
#
#
def trade_num(array, cnt): #
    global result #
    if cnt == trade: #
        if result < array: #
            result = array #
        return #

    if max_numbers == array: #
        if (trade - cnt)%2 == 0: #
            result = max_numbers #
            return #
        for i in range(len(array)-1): #
            for j in range(i+1,len(array)): #
                new_arr = array[:] #
                new_arr[i],new_arr[j] = new_arr[j],new_arr[i] #
                new_value = new_arr #
                if new_value not in dist[cnt]: #
                    trade_num(new_arr, cnt + 1) #
                    dist[cnt].append(new_value) #

    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i] < array[j]:
                new_arr = array[:]
                new_arr[i],new_arr[j] = new_arr[j],new_arr[i]
                new_value = new_arr
                if new_value not in dist[cnt]:
                    trade_num(new_arr, cnt + 1)
                    dist[cnt].append(new_value)


T = int(input()) #
for tc in range(1,T+1): #
    numbers, trade = input().split() #
    trade = int(trade) #
    numbers = list(map(int,numbers)) #
    dist = {i : [] for i in range(trade + 1)} #
    max_numbers = (sorted(numbers, reverse=True)) #
    result = [] #
    trade_num(numbers, 0) #
    print('#{} {}'.format(tc,''.join(map(str,result)))) #
