def getGuessedWord(secreWord, lettersGuessed):
    result = ''
    for c in secretWord:
        if c in lettersGuessed:
            result += c
        else:
            result += '_'
    return result


secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getGuessedWord(secretWord, lettersGuessed)