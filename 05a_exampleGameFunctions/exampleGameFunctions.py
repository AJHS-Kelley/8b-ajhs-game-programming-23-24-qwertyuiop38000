# Example Game Functions Projects, William Castengera, v0.4
import random

character = str(input("Choose a character Ivan, Chad or Jim"))
enemyList = ['hobgoblin', 'hellhound', 'cobalt', 'orc', 'troglodyte', 'wolf']
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

def enemyAppears():
    enemyIndex = random.randint(0, len(enemyList) - 1)
    enemyName = enemyList(enemyIndex)

def functionfour(param1, param2, param3):
    pass
#damage = damageDone(isCritical, character)
#print(damage)
enemyAppears()