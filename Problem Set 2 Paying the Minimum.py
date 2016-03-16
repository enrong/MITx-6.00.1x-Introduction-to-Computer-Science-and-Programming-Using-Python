balance = 5000
annualInterestRate = 0.18
monthlyinterestrate = annualInterestRate/12
upbalance = balance
monthlyPaymentRate = 0.02
i=-1
totalPaid = 0

while i < 12:
    i += 1
    minimummonthlypayment = upbalance*monthlyPaymentRate
    upbalance = (upbalance - minimummonthlypayment)*(1+ monthlyinterestrate)
    print ('Mouth: '+ str(i))
    print ('Minimum monthly payment:' + str(round(minimummonthlypayment,2)))
    print ('Remaining balance: ' + str(round(upbalance,2)))
    totalPaid += minimummonthlypayment
print ('Total paid:' +str(round(totalPaid,2)))
print ('Remaining balance:' + str(round(upbalance,2)))