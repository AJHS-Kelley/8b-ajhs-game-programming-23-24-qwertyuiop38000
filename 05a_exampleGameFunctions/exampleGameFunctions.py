# Example Game Functions Projects, William Castengera, v0.4
import random

character = str(input("Choose a character Ivan, Chad or Jim"))
enemyList = {'city': 'rat,raven,Monkey Spider,dog,crocodile'.split(','),
 'swamp': 'ghast orc troll snake dragon'.split(), 
 'forest': 'square rectangle triangle rhombus kite trapezoid pentagon hexagon octogon nonagon'.split(),
  'dungeon': 'corn peas broccoli potatoe beef chicken carrot radish banana people'.split()}
secretNumber = 2.8
secretNumber += 1
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

def enemyAppears(place='tutorial',listName=enemyList):
    if place == 'city':
        pass
    elif place == 'swamp':
        pass
    elif place == 'forest':
        pass
    elif place == 'dungeon':
        pass
    else:
        index = random.randint(0, len(listName) - 1)
        name = listName(index)

def functionfour(param1, param2, param3):
    pass
#damage = damageDone(isCritical, character)
#print(damage)
locationList = ["swamp", 'forest', 'city', 'dungeon']
location = input("Where would you like to go?\nSwamp\nForest\nCity\nDungeon\n")
location = location.lower()
while location not in locationList:
    print('that is not right choose again')
    locationList = ["swamp", 'forest', 'city', 'dungeon']
    location = input("Where would you like to go?\nSwamp\nForest\nCity\nDungeon\n")
print(f'Ps the secret number is {secretNumber}')