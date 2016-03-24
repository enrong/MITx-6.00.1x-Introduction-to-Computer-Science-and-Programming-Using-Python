def uniqueValues(aDict):
    result = []
    for k in aDict.keys():
        samecount = 0
        for b in aDict.values():
            if aDict[k] == b:
                samecount += 1
        if samecount == 1:
            result.append(k)
        print samecount
    result.sort()
    return result

print uniqueValues({2: 2, 5: 0, 7: 3})
