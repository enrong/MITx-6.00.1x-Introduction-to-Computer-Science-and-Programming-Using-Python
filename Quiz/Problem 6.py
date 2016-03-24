def count7(N):
    countDigit = 0
    if N % 10 ==7:
        countDigit += 1
    if N > 6:
        return count7(N/10) + countDigit
    return 0
print count7(717717777777)
