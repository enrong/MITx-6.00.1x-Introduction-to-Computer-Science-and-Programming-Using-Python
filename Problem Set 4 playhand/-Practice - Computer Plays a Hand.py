def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score = 0
    m = n
    rehand = hand.copy()
    def newdisplayHand(hand):
        result = ''
        for letters in hand.keys():
            for j in range(hand[letters]):
                result += letters +' '
        return result
    
    
    while m > 0 :
        word = compChooseWord(rehand, wordList, n)
        if word == None:
            break
        print 'Current Hand:',newdisplayHand(rehand)
        score += getWordScore(word, n)
        print "'"+word+"'", 'earned',getWordScore(word, n),'points. Total score:',score,'points'
        m -= len(word)
        rehand = updateHand(rehand, word)
    print 
    if sum(rehand.values()) != 0 : 
        print 'Current Hand:',newdisplayHand(rehand)
    print 'Total score:',score,'points.'

