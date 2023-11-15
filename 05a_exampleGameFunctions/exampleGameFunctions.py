# Example Game Functions Projects, William Castengera, v0.2
import random

character = str(input("Choose a character Ivan, Chad or Jim"))
enemyList = ['hobgoblin', 'hellhound', 'cobalt', 'orc', 'troglodyte', ]
def criticalHit():
    hit = random.randint(1, 20)
    if hit == 20:
        return True
    else:
        return False
isCritical = criticalHit()
def damageDone(isCrit, char):
    if isCritical == True:
        if character == "Chad":
            damage = random.randint(250, 300)
            return damage
        elif character == "Ivan":
            damage = random.randint(250, 300)
            return damage
        else:
            damage = random.randint(200, 250)
            return damage
    else:
        damage = random.randint(100, 150)
        return damage

def functionThree(param1 = "default value"):
    pass

def functionfour(param1, param2, param3):
    pass
damage = damageDone(isCritical, character)
print(damage)