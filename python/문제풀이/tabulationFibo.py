### bottom up approach
### list 접근
def fib_tab(n):
    tab=[0,1,1]
    for i in range(3,n+1):
        tab.append(tab[i-1]+tab[i-2])
    return tab[n]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))

### dictionary접근
def fib_tab(n):
    fib_cache = {1:1, 2:1}
    # if n > 2:
    for i in range(3, n+1):
        fib_cache[i]=fib_cache[i-2]+fib_cache[i-1]
    return fib_cache[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))