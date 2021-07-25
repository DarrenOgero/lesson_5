def fact(n):
    pr=1
    a=[]
    for i in range(1, n+1, 2):
        pr=pr*i
        a.append(i)
    return a

print(fact(21))