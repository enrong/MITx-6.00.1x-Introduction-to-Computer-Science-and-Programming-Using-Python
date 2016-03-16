'''
example = 'abcdefghijklmnopqrstuvwxyz'

s = 'azcbobobegghakl'

s = 'abc'
result = 0
count = 0
target = ''
finaltarget = ''
for i in range(0,len(s)-1):
    for j in range (0,len(example)-1):
        if s[i:i+1] == example[j:j+1]:
            count += 1
            if result < count:
                result = count
                target  += s[i]
                if len(finaltarget) < len(target):
                    finaltarget = target
        else:
            target = ''
            count = 0
print finaltarget
print result

'''

s = 'azcbobobegghakl'
longeststr = ''
currentstr = s[0]
for i in range(0,len(s)-1):
    if s[i] <= s[i+1]:
        currentstr += s[i+1]
        if len(currentstr)>len(longeststr):
            longeststr = currentstr
    else:
        currentstr = s[i+1]
    print currentstr
print longeststr