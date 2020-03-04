# 조합 구하는 함수
def combination(lst, r):  # lst : 전체 리스트, r : 몇개씩 뽑을 것인지
    def gene(choose):
        if len(choose) == r:  # 전체리스트에서 r개를 뽑으면 combi 배열에 넣고 종료하는 조건
            # print(choose)
            tmp = choose[:]
            combi.append(tmp)
            return
        if choose:
            start = lst.index(choose[-1]) + 1
        else:
            start = 0
        for next in range(start, len(lst)):
            choose.append(lst[next])
            gene(choose)
            choose.pop()
    gene([])

player = [x for x in range(N)]
combi = []
combination(player, len(player)//2)  #
# print(combi)
