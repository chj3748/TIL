def merge(list1, list2):
    i=0
    j=0
    result=[]
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            result.append(list1[i])
            i+=1
        else:
            result.append(list2[j])
            j+=1
    if i==len(list1):
        for l2 in range(j,len(list2)):
            result.append(list2[l2])
    if j==len(list2):
        for l1 in range(i,len(list1)):
            result.append(list1[l1])
    return result
# 합병 정렬
def merge_sort(my_list):
    if len(my_list)<2:
        return my_list
    l=len(my_list)//2
    return merge(merge_sort(my_list[:l]),merge_sort(my_list[l:]))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
