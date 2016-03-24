def primesList(N):
    pnList =[]
    for i in range(2 ,N+1 ):
        count = 0
        for j in range(2 ,i ):
            if i % j == 0:
                count += 1
        if count == 0:
            pnList.append(i)
    return pnList

print primesList(1000)