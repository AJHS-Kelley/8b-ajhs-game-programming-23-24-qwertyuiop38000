# DNA Replication Game, William Castengera, v0.2

# Import Entire Modules -- Get the whole tool box.
import  time, datetime 

# Importing Specific Methods -- Get the specific tool
from random import choice

# Store the DNA Bases
dnaBases = ["A", "T", "G", "C"]

# GAME FUNCTIONS
def gameIntro() -> None:
    pass

def genDna() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please enter a positive integer number of bases to generate\n"))
    dnaSequence = ""
    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    return dnaSequence

dna = genDna()
print(dna)

