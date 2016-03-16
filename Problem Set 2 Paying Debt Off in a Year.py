balance = 5000
annualInterestRate = 0.18
monthlyinterestrate = annualInterestRate/12
upbalance = balance
currentPayment = 0

while  upbalance > 0:
    currentPayment += 10
    month = 0
    upbalance = balance
    
    while month < 12 and upbalance > 0:
        month += 1
        upbalance -= currentPayment
        upbalance += upbalance * monthlyinterestrate
        print str(month)
        print str(upbalance)
lowestPayment = currentPayment
print str(lowestPayment)
print str(upbalance)
     










