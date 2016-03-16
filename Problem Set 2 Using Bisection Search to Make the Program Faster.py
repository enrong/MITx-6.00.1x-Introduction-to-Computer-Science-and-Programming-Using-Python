balance = 5000
annualInterestRate = 0.18
monthlyinterestrate = annualInterestRate/12
upbalance = balance
epsion = 0.01
'''
high = (((1+monthlyinterestrate)**12)*balance)/12
'''
high =  (balance * (1 + monthlyinterestrate)**12) / 12
low = balance/12

print high
print low
numberofguesses = 0

currentPayment = (high + low)/2.0
lowestPayment = currentPayment
print currentPayment 


while abs(upbalance) >= epsion:
    month = 0
    upbalance = balance
    print ('currentPayment: '+ str(currentPayment))
    for month in range(0,12):
        upbalance = (upbalance - currentPayment)*(1+monthlyinterestrate)
    if upbalance >= 0:
        low = currentPayment
    else:
        high = currentPayment
    currentPayment = (low + high)/2.0
    

lowestPayment = currentPayment
print str(lowestPayment)
print str(upbalance)
