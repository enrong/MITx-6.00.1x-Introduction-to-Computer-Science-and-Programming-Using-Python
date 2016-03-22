import string
def getAvailableLetters(lettersGuessed):
    result = ''
    for c in string.ascii_lowercase:
        if c not in lettersGuessed:
            result += c
    return result

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)