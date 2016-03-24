def satisfiesF(L):
    for i in range(len(L)):
        if not f(L[i]):
            L[i] = None
    L1 = L[:]
    for j in range(len(L1)):
        if L1[j] == None:
            L.remove(None)
    return len(L)

run_satisfiesF(L, satisfiesF) 
