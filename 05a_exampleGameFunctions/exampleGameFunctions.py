# Example Game Functions Projects, William Castengera, v1.1
import random

character = str(input("Choose a character Ivan, Chad or Jim"))
enemyList = {'city': 'rat,raven,Monkey Spider,dog,crocodile'.split(','),
 'swamp': 'ghast orc troll snake dragon'.split(), 
 'forest': 'leopard tiger panther centaur boar'.split(),
  'dungeon': 'goblin slime undead basilisk phoenix'.split()}
secretNumber = 2.8
secretNumber += 1
def criticalHit():
    hit = random.randint(1, 20)
    if hit == 20:
        return True
    else:
        return False
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
        enemy = listName['city'][random.randint(1, len(listName['city']) - 1)]
        print(enemy)
    elif place == 'swamp':
        enemy = listName['swamp'][random.randint(1, len(listName['swamp']) - 1)]
        print(enemy)
    elif place == 'forest':
        enemy = listName['forest'][random.randint(1, len(listName['forest']) - 1)]
        print(enemy)
    elif place == 'dungeon':
        enemy = listName['dungeon'][random.randint(1, len(listName['dungeon']) - 1)]
        print(enemy)
    else:
        keyList = ['city', 'dungeon', 'swamp', 'forest']
        keyPick = keyList[random.randint(1, len(keyList)-1)]
        enemy = listName[keyPick][random.randint(1, len(listName[keyPick]) - 1)]
    return enemy

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

opponent = enemyAppears(location, enemyList)
isCritical = criticalHit()
dam = damageDone(isCritical, character)
def fight(howHurty, badBoy):
    playerHealth = 5000
    attack = 0
    enemyHealth = 500
    print('A wild  ' + badBoy + ' appeared!\n')
    print(f"Your health is {playerHealth}\nThe {badBoy}'s health is {enemyHealth}\n")
    haveAttacked = input('Type A to attack')
    haveAttacked = haveAttacked.upper()
    while enemyHealth > 0:
        if attack == 3:
            enemyAttackDamage = random.randint(50, 100)
            playerHealth = playerHealth - enemyAttackDamage
            print('The ' + badBoy + ' has attacked you leaving you with ')
            print(playerHealth)
            print(' health')
        if haveAttacked == 'A':
            enemyHealth = enemyHealth - howHurty
            if enemyHealth <= 0:
                print('You have slain the ' + badBoy)
            else:
                print(enemyHealth)
                haveAttacked = input('\nType A to attack')
                haveAttacked = haveAttacked.upper()
        attack += 1
fight(dam, opponent)


print(f'your secret number is {secretNumber}')