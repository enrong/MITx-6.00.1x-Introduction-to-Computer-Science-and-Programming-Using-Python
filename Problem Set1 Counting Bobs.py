s = 'azcbobobegghakl'
'''
print ('Number of times bob occurs is:' + str(s.count('bob')))
'''

count = 0
for i in range(0,len(s)-1):
    if s[i:i+3] == 'bob':
        count += 1
        print count
print ('Number of times bob occurs is:' + str(count))
