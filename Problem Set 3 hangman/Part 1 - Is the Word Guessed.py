def isWordGuessed(secretWord, lettersGuessed):
    result = ''
    for c in lettersGuessed:
        if c in secretWord:
            result += c
    for e in secretWord:
        if e not in result:
            return False
    return True     
    

secretWord = 'apple' 
lettersGuessed = ['a', 'p', 'l', 'e']
print isWordGuessed(secretWord, lettersGuessed)