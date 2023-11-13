# Example Game Functions Projects, William Castengera, v0.2
import random

character = input("Choose a character Ivan, Chad or Jim")

def criticalHit():
    hit = random.randint(1, 20)
    if hit == 20:
        return True
    else:
        return False
def damageDone(isCritical, character):
    isCritical = criticalHit()
    if isCritical == True and character == "Jim":
        damage = random.randint()

def functionThree(param1 = "default value"):
    pass

def functionfour(param1, param2, param3):
    pass