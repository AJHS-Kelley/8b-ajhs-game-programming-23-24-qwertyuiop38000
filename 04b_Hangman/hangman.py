# Hangman Game by William Castengera, v1.0
import random
#words = 'cat dog wolf bird fish cow sheep cone two one dance sweep broom icecream fisher apple banana pickle pirate puruse abruptly absurd abyss affix askew avenue awkward axiom azure bagpipes'.split()
#dictionary version
# stored in key:value pairs.
# Actual Dictionary word (key) : Value (definition)
# uses {}to specify a dictionary.
words = {'Colors': 'red orange yellow green blue indigo violet silver gold black'.split(),
 'Animals': 'cat dog wolf bird fish cow sheep lion alligator giraffe'.split(), 
 'Shapes': 'square rectangle triangle rhombus kite trapezoid pentagon hexagon octogon nonagon'.split(),
  'food': 'corn peas broccoli potatoe beef chicken carrot radish banana people'.split()}


# Variable names in all caps are constants and not meant to change
HANGMAN_BOARD = ['''
    +---+
        |
        |
        |
     =======''','''
    +---+
    0   |
        |
        |
     =======''','''
     +---+
    0   |
    |   |
        |
     =======''','''
    +---+
    0   |
   /|   |
        |
     =======''','''
     +---+
    0   |
   /|\  |
        |
     =======''','''
    +---+
    0   |
   /|\  |
   /    |
     =======''','''     
    +---+
    0   |
   /|\  |
   / \  |
     =======''', '''
    +---+
    0   |
  o-|-o |
   / \  |
     =======''', '''
    +---+
    0   |
  o-|-o |
   / \  |
  o   o |
     =======''']

# Pick Word from List
def getRandomWord(wordList): # Return a random wprd from the list
    wordIndex = random.randint(0, len(wordList) - 1)
    # len(listname) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
    return wordList[wordIndex]

# Pick word from dictionary
def getRandomWord(wordDict): # Return a random wprd from the list
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey])-1)
    return [wordDict[wordKey][wordIndex], wordKey]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = '')
    print()
    
    blanks = '_' * len(secretWord)

    # Replace Blanks with Correct Letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Please guess a letter and press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter only 1 letter.')
        elif guess in alreadyGuessed:
            print('letter has been guessed already, please try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('thats not a letter do better')
        else:
            return guess

def playAgain():
    print('do you want to play again? yes or no?')
    return input().lower().startswith('y')

# Introduce the Game
print('hangman now')

# choose difficulty
difficulty = 'X'
while difficulty not in 'EMH':
    print('choose a difficulty easy medium or hard only type first letter')
    difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
if difficulty == 'H':
    del HANGMAN_BOARD[8]
    del HANGMAN_BOARD[7]
    del HANGMAN_BOARD[5]
    del HANGMAN_BOARD[3]


missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

# Main game loop
while True:
    print('The secret word is from the ' + secretSet + ' category.\n')
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # check if win
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('you suck at losing')
            print('The secret word was ' + secretWord)
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        
        if len(missedLetters) == len(HANGMAN_BOARD) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('you are very good at losing')
            print('You made this number of correct Guesses ' + str(len(correctLetters)))
            print('tehe secret word was ' + secretWord)
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break












# i = 0
# while i < 50:
#     word = getRandomWord(words)
#     print(word)
#     i += 1


