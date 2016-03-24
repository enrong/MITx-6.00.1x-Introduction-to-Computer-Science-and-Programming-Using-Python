def isValidWord(word, hand, wordList):
    result = hand.copy()
    if len(word) == 0:
        return False
    for i in word:
        if result.get(i, 0) > 0:
            result[i]= result.get(i, 0) - 1
        else:
            return False
    for l in wordList:
        if l == word:
            return True
    return False
