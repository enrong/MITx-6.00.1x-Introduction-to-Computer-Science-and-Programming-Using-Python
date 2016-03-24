def updateteHand(hand,word):
    result = hand.copy()
    for i in word:
        result[i] -= 1
    return result

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word = 'aqllumi'
print updateteHand(hand,word)
print hand
