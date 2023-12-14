# Dice Roling Module by Wiliam Castengera, v0.0
import random

def roll(numDice, sizeDice): # Verified Working 12-14-23
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        numRolled += 1
        sum += roll
    return sum 

def display(numDice, sizeDice): # Verified Working 12-14-23
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        print(f"Roll: {roll}\n")
        numRolled += 1
        sum += roll
        print(f"Sum: {sum}\n")
    return sum

def isDoubles(roll1, roll2):
    if roll1 == roll2:
        isDoubles = True
    else:
        isDoubles = False
    return isDoubles

def isExploding(roll, sizeDice):
    if roll == sizeDice:
        isExploding = True
    else:
        isExploding = False
    return isExploding

