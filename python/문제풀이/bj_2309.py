import itertools
h=100
members=[]
for _ in range(9):
    members.append(int(input()))
powersets = list(itertools.combinations(members, 7))
for powerset in powersets:
    if sum(powerset) == h:
        result = list(powerset)
        break
result.sort()
for dwarf in result:
    print(dwarf)
