import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):

    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):

    new = ""
    for i in secretWord:
        if i in lettersGuessed:
            new += i
            if new == secretWord:
                return True
        else:
            return False


def getGuessedWord(secretWord, lettersGuessed):

    result = list(secretWord)
    for i in result:
        if i not in lettersGuessed:
            result[result.index(i)] = " _ "
    transtring = ''.join(result)
    return transtring


def getAvailableLetters(lettersGuessed):

    Alletters = string.ascii_lowercase
    result = list(Alletters)
    for i in lettersGuessed:
        if i in result:
            result.remove(i)
    transtring = ''.join(result)
    return transtring    

def hangman(secretWord):
 
    intro = str(len(secretWord))
    lettersGuessed = []
    guess = str
    mistakesMade = 8
    wordGuessed = False
    
    print 'Welcome to the game, Hangman!'
    print ('I am thinking of a word that is ') + intro + (' letters long.')
    print ('------------')
 
    while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print ('You have ') + str(mistakesMade) + (' guesses left.')
        print ('Available letters: ') + getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print ("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
            else:
                lettersGuessed.append(guess)
                print ('Good guess: ') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
        else:
            if guess in lettersGuessed:
                print ("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
            else:
                lettersGuessed.append(guess)
                mistakesMade -= 1
                print ('Oops! That letter is not in my word: ') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
 
    if wordGuessed == True:
        return 'Congratulations, you won!'
    elif mistakesMade == 0:
        print ('Sorry, you ran out of guesses. The word was ') + secretWord

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
