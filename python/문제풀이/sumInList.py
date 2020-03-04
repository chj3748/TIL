### 시간복잡도 O(n^2)
# def sum_in_list(search_sum, sorted_list):
#     for i in range(len(sorted_list)-1):
#         for j in range(i+1,len(sorted_list)):
#             result=sorted_list[i]+sorted_list[j]
#             if result==search_sum:
#                 return True
#             elif result>search_sum:
#                 break
#     return False


#### 시간복잡도 개선 O(n)
# def sum_in_list(search_sum, sorted_list):
#     h=0
#     t=len(sorted_list)-1
#     while h<t:
#         result= sorted_list[h]+sorted_list[t]
#         if result==search_sum:
#             return True
#         elif result<search_sum:
#             h+=1
#         else:
#             t-=1
#     return False

### 다른 참신한 방법 O(2n)
def sum_in_list(search_sum, sorted_list):
    dic_list={}
    for i in sorted_list:
        dic_list[i]=True
    for i in sorted_list:
        if dic_list.get(search_sum-i):
            return True
    else:
        return False

print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))