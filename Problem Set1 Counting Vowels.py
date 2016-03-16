s = 'azcbobobegghakl'
'''
def numberofvowel(s):
    result = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
    return result
print ('Number of vowels: ' + str(numberofvowel(s)))
'''

count = 0
for c in s:
    if c in ('aeiou'):
        count += 1
print ('Number of vowels:' + str(count)) 
