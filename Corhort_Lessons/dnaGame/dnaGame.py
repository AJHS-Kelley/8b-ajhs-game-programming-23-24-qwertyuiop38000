# DNA Replication Game, William Castengera, v0.3

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

def genRNA(dnaSequence: str) -> tuple:
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan, 01, 1970
    print(f"The DNA sequence is {dnaSequence}.\n")
    print("You will generate the RNA sequence that would match.\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence.\n")
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan, 01, 1970
    rnaSequence = input("Please enter the matching RNA. Leave No spaces! then press enter. Be fast!\n").upper()
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime)
    # Tuples are ORDERED -- you can reference elements with the index
    # Tuples are UNCHANGEABLE -- you cannot add, modify or delete elements are creating
    # Tuples CAN have duplicate values.

rna = genRNA(dna)
print(rna)
