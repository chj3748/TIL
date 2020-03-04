# def select_stops(water_stops, capacity):
#     diff=[0]*(len(water_stops)-1)
#     for i in range(len(water_stops)-1):
#         diff[i]=water_stops[i+1]-water_stops[i]
#
#     for i in diff:
#         if i > capacity:
#             return 0
#     return 1

# def select_stops(water_stops, capacity):
#     #1km당 1L의 물을 마셔야 한다.
#     #이 함수는 산을 오르며 들러야 할 약수터의 위치 리스트를 반환한다.
#     #등산하기 전에는 이미 물통이 가득 채워져 있으며, 약수터에 들르면 늘 물통을 가득 채움.
#     #항상 가능한 먼 약수터로 가는 것이 최선의 선택
#
#     new_list = []       #들러야 하는 약수터의 리스트
#     temp_capacity = capacity   #임시 물통, 산을 오르기 전 물통은 가득 채워져 있다고 가정한다.
#
#     for i in range(0, len(water_stops)-1):
#         if i == 0:
#             temp_capacity = temp_capacity - water_stops[i]
#         else:
#             temp_capacity = temp_capacity - (water_stops[i] - water_stops[i-1])    #1km당 1L소모하니 산을 오르며 capacity의 용량을 걸은만큼 감소
#
#         if temp_capacity < (water_stops[i+1] - water_stops[i]):    #다음 행선지와 현재 약수터의 거리보다 현재 갖고있는 물 양이 적다면 무조건 채워야한다.
#             new_list.append(water_stops[i])
#             temp_capacity = capacity    #물통 가득 채우기
#     return new_list+[water_stops[-1]]

def select_stops(water_stops, capacity):
    # 약수터 위치 리스트
    stop_list = []

    # 마지막 들른 약수터 위치
    prev_stop = 0

    for i in range(len(water_stops)):
        # i 지점까지 갈 수 없으면, i - 1 지점 약수터를 들른다
        if water_stops[i] - prev_stop > capacity:
            stop_list.append(water_stops[i - 1])
            prev_stop = water_stops[i - 1]

    # 마지막 약수터는 무조건 간다
    stop_list.append(water_stops[-1])

    return stop_list


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))