SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

HAND_SIZE = 7
n = HAND_SIZE


def getWordScore(word):
    result = 0
    for i in word:
        result += SCRABBLE_LETTER_VALUES[i]
        
    if len(word) == n:
        return result * len(word) + 50
    return result * len(word)


print getWordScore('')
print getWordScore('weed')

print getWordScore('waybill')