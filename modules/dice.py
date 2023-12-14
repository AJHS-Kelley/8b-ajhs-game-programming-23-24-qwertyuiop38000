# Dice Roling Module by Wiliam Castengera, v0.0
import random

def rollDice(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        print(f"Roll: {roll}\n")
        numRolled += 1
        sum += roll
        print(f"Sum: {sum}\n")
    return sum 