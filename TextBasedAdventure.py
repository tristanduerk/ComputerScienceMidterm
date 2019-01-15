from __future__ import print_function

# test = input("Input something: ")
# print(test)
maxX = 3
maxY = 3
xPosition = 0
yPosition = 0

class Tile:
    isValid = False
    hasEncounter = False
    hasWeapon = False
    hasKey = False
    hasMonster = False
    hasChalice = False
    
class Person:
    holdingWeapon = False
    holdingChalice = False
    holdingKey = False
    
person = Person()

map = [[Tile() for j in range(maxY)] for i in range(maxX)]
map[0][0].isValid = True
map[0][1].isValid = True
map[0][2].isValid = True

map[1][0].isValid = True
map[1][1].isValid = True
map[1][2].isValid = True

map[2][0].isValid = True
map[2][1].isValid = True
map[2][2].isValid = True

map[2][0].hasEncounter = True
map[2][0].hasWeapon = True

def encounter(newX, newY):
    global xPosition, yPosition
    if (map[newX][newY].hasWeapon):
        person.holdingWeapon = True
        print("You have encountered an object! It is a weapon. You picked it up!")
    elif (map[newX][newY].hasKey): 
        person.holdingKey = True   
        print("You have encountered an object! It is a key. You picked it up!")
    elif (map[newX][newY].hasChalice):
        person.holdingChalice = True
        print("You have encountered an object! It is a chalice. You picked it up!")
    elif (map[newX][newY].hasMonster):
        fightOrFlight = input("You encountered a monster! Would you look to fight it or run away?")
        if fightOrFlight.lower() == "fight":
            if person.holdingWeapon == True:
                print("You killed the monster!")
            else:
                print("You died! You are now back at spawn.")
                xPosition = 0
                yPosition = 0
        else:
            print("You have successfully fled.")

def move(direction):
    global xPosition, yPosition
    newX = xPosition
    newY = yPosition
    if (direction.lower() == ("north")):
        newY -= 1
    if (direction.lower() == ("south")):
        newY += 1
    if (direction.lower() == ("east")):
        newX += 1
    if (direction.lower() == ("west")):
        newX -= 1
    if (newX >= 0 and newX < maxX and newY >= 0 and newY < maxY):
        if (map[newX][newY].isValid):
            xPosition = newX
            yPosition = newY
            if (map[newX][newY].hasEncounter):
                encounter(newX, newY)
            else:
                print("You have successfully moved.")
        else: print("You hit a wall.")
    else: print ("You hit a wall.")
    
while(True):
    direction = input("What direction do you want to go? ")
    move(direction)
