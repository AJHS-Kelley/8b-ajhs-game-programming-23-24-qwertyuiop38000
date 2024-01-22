# DNA Replication Game, William Castengera, v0.3
import os
# Import Entire Modules -- Get the whole tool box.
import  time, datetime 

# Importing Specific Methods -- Get the specific tool
from random import choice
i = 0
# Store the DNA Bases
dnaBases = ["A", "T", "G", "C"]

# GAME FUNCTIONS
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please enter a positive integer number of bases to generate\n"))
    dnaSequence = ""
    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    return dnaSequence

def doTranscription(dnaSequence: str, i: int) -> tuple:
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan, 01, 1970
    print(f"The DNA sequence is {dnaSequence}.\n")
    print("You will generate the RNA sequence that would match.\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence.\n")
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan, 01, 1970
    rnaSequence = input("Please enter the matching RNA. Please put spaces between each letter! then press enter. Be fast!\n").upper().split()
    while len(rnaSequence) > i:
        if rnaSequence[i] not in "AUCG":
            print("you lose")
            break
        else:
            i += 1
            continue
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime)
    # Tuples are ORDERED -- you can reference elements with the index
    # Tuples are UNCHANGEABLE -- you cannot add, modify or delete elements are creating
    # Tuples CAN have duplicate values.

def verifySequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    if len(dnaSequence) != len(rnaSequence):
        print("the sequences are different lengths and therefore do not match\n")
        return isMatch
    for dnaBase, rnaBase in zip(dnaSequence, rnaSequence):
        if dnaBase == "A" and rnaBase == "U":
            isMatch = True
        elif dnaBase == "C" and rnaBase == "G":
            isMatch = True
        elif dnaBase == "G" and rnaBase == "C":
            isMatch = True
        elif dnaBase == "T" and rnaBase == "A":
            isMatch = True
        else:
            print("No match womp womp")
    return isMatch

def calcScore(rnaSequence: str, rnaTime: float) -> int:
    score = 0
    if rnaTime < 1.0:
        score += 1000000
    elif rnaTime < 5.0:
        score += 900000
    elif rnaTime < 15.0:
        score += 100000
    elif rnaTime < 25.0:
        score += 50000
    else:
        score += 1

    scoreMulti = 0.0
    if len(rnaSequence) >= 30:
        scoreMulti = 5.0
    elif len(rnaSequence) >= 15:
        scoreMulti = 2.5
    elif len(rnaSequence) >= 5:
        scoreMulti = 1.0
    else:
        scoreMulti = 0.001
    score *= scoreMulti
    return score

def saveScore(dnaSequence: str, rnaSequence: str, rnaTime: float, score: int) -> None:
    playerName = input("What is your first name?\n")
    lastName = input("what is your last name?\n")
    fullName = playerName + " " + lastName

    fileName = "dnaReplicationScore" + fullName + ".txt"
    saveData = open(fileName, "a")
    # File Modes
    # "x" mode -- CREATE FILE, IF FILE EXISTS, EXIT WITH ERROR
    # "w" mode -- CREATE FILE, IF FILE EXISTS, OVERWRITE IT
    # "a" mode -- CREATE FILE, IF FILE EXISTS, APPEND TO IT
    saveData.write(f"DNA sequence: {dnaSequence}\nRNA Sequence: {rnaSequence}\n")
    saveData.write(f"Transcription Time: {rnaTime}\n")
    saveData.write(f"Score: {score}\n")
    saveData.write(f"{fullName}\n")
    saveData.write(f"{datetime.datetime.now()}\n")
    saveData.close()




dna = genDNA()
rna = doTranscription(dna, i)
if verifySequence(dna, rna[0]):
    score = (calcScore(rna[0], rna[1]))
    saveScore(dna, rna[0], rna[1], score)


