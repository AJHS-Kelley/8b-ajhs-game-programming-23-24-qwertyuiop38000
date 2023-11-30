import random
# funciton -- a named piece of code that can be reused easily.
# function signature -- syntax for creating a new function
def exampleFunctionA():#no parameters
    count = 0
    num = int(input("how many times do want to wish happy birthday?\n"))
    while count < num:
        print("Happy Birhtday\n")
        count += 1

def exampleFunctionB(num, count): #parameters
    while count < num:
        print("happy birthday")
        count += 1

# IF A FUNCTION REQUIRES PARAMETERS, YOUR CODE WILL CRASH WITHOUT THEM! 

# running a function is known as calling the function
# exampleFunctionA()
# exampleFunctionB(100, 0)

def rollDice(numDice, sizeDice):
    numRolled = 0
    sum = 0
    while numRolled < numDice:
        roll = random.randint(1, sizeDice)
        print(f"Roll: {roll}\n")
        numRolled += 1
        sum += roll
        print(f"Sum: {sum}\n")
    return sum # return will immediatly exit a function, loop, or if/elif/else block.

# rollDice(1, 20)
# rollDice(10, 100)

stengthPlayer = rollDice(3, 6)
dexterityPlayer = rollDice(3, 6)
wisdomPlayer = rollDice(3, 6)

print(stengthPlayer)
print(dexterityPlayer)
print(wisdomPlayer)

def genStats():
    playerStats = [
        0, # STRENGTH
        0, # DEXTERITY
        0, # CONSTITUTION
        0, # INTELLIGENCE
        0, # WISDOM
        0  # CHARISMA
    ]
    i = 0
    while i < len(playerStats):
        playerStats[i] = rollDice(3, 6)
        i += 1

    print(playerStats)

genStats()



