from __future__ import print_function

# test = input("Input something: ")
# print(test)
maxX = 20
maxY = 20
xPosition = 0
yPosition = 0

class Tile:
    isValid = False
    hasEncounter = False
    hasWeapon = False
    hasKey = False
    hasMonster = False
    hasChalice = False
    hasWinCondition = False
    hasLockedDoor = False
    isRoomEntrance = False
    isPillar = False

    roomDescription = ""
    
class Person:
    holdingWeapon = False
    holdingChalice = False
    holdingKey = False
    
person = Person()

map = [[Tile() for j in range(maxY)] for i in range(maxX)]

# Entrance Room
for i in range(0, 5):
        for j in range(0, 5):
            map[i][j].isValid = True

# Exit to Hallway
map[3][4].hasEncounter = True
map[3][4].isRoomEntrance = True
map[3][4].roomDescription = "This is the room you started in, bring the chalice back to the starting position to win the game!"

# Starting Point is Winning Spot
map[0][0].hasEncounter = True
map[0][0].hasWinCondition = True

# Pillars
map[0][3].isPillar = True
map[0][3].isValid = False
map[1][2].isPillar = True
map[1][2].isValid = False
map[3][1].isPillar = True
map[3][1].isValid = False
map[3][3].isPillar = True
map[3][3].isValid = False

# Connecting Hallway
for i in range(1, 6):
    for j in range(6, 10):
        map[i][j].isValid = True

# Hallway Entrance
map[3][5].isValid = True
map[3][5].hasEncounter = True
map[3][5].isRoomEntrance = True
map[3][5].roomDescription = "This room is barren, however, there are two exits. Which path will you choose?"

# Hallway Exit to Armory
map[3][9].isValid = True
map[3][9].hasEncounter = True
map[3][9].isRoomEntrance = True
map[3][9].roomDescription = "HI"

# Hallway Exit to Main Hall
map[6][8].isValid = True
map[6][8].hasEncounter = True
map[6][8].isRoomEntrance = True
map[6][8].roomDescription = "HI"

#Pillar
map[4][8].isPillar = True
map[4][8].isValid = False

# Armory
for i in range(1, 5):
    for j in range(11, 17):
        map[i][j].isValid = True
for i in range(0, 6):
    map[i][17].isValid = True

# Armory Entrance / Exit
map[3][10].isValid = True
map[3][10].hasEncounter = True
map[3][10].isRoomEntrance = True
map[3][10].roomDescription = "Hi"

# Pillar
map[2][13].isPillar = True
map[2][13].isValid = False

# Weapons
map[0][17].hasEncounter = True
map[0][17].hasWeapon = True
map[5][17].hasEncounter = True
map[5][17].hasWeapon = True

# Main Hall
for i in range(7, 17):
    for j in range(4, 12):
        map[i][j].isValid = True

# Hall Entrance
map[7][8].isValid = True
map[7][8].hasEncounter = True
map[7][8].isRoomEntrance = True
map[7][8].roomDescription = "Hi"

# Hall Exit
map[12][11].isValid = True
map[12][11].hasEncounter = True
map[12][11].isRoomEntrance = True
map[12][11].roomDescription = "Hi"

# Pillars
map[9][6].isPillar = True
map[9][6].isValid = False
map[11][6].isPillar = True
map[11][6].isValid = False
map[12][6].isPillar = True
map[12][6].isValid = False
map[14][6].isPillar = True
map[14][6].isValid = False

map[9][9].isPillar = True
map[9][9].isValid = False
map[11][9].isPillar = True
map[11][9].isValid = False
map[12][9].isPillar = True
map[12][9].isValid = False
map[14][9].isPillar = True
map[14][9].isValid = False

# Random Monster
map[12][8].hasEncounter = True
map[12][8].hasMonster = True

# Key to private chamber
map[16][11].hasEncounter = True
map[16][11].hasKey = True

# Private Chamber
for i in range(10, 16):
    for j in range(13, 17):
        map[i][j].isValid = True

# Private Chamber Entrance/Exit
map[12][13].isValid = True
map[12][13].hasEncounter = True
map[12][13].isRoomEntrance = True
map[12][13].roomDescription = "Hi"

# Locked Door
map[12][12].isValid = True
map[12][12].isRoomEntrance = True
map[12][12].hasLockedDoor = True

# Monsters guarding chalice
map[11][16].hasEncounter = True
map[11][16].hasMonster = True
map[12][15].hasEncounter = True
map[12][15].hasMonster = True
map[13][16].hasEncounter = True
map[13][16].hasMonster = True

# Chalice
map[12][16].hasEncounter = True
map[12][16].hasChalice = True


def encounter(newX, newY, direction):
    global xPosition, yPosition
    if (map[newX][newY].hasWeapon):
        person.holdingWeapon = True
        print("You have encountered an object! It is a weapon. You picked it up!")
    elif (map[newX][newY].hasKey): 
        person.holdingKey = True   
        print("You have encountered an object! It is a key. You picked it up!")
    elif (map[newX][newY].hasChalice):
        person.holdingChalice = True
        print("You have encountered an object! It is a chalice. You picked it up! Bring it back to the start to win!")
    elif (map[newX][newY].hasWinCondition and person.holdingChalice):
        print("Congratulations! You win!")
        # quit()
    elif (map[newX][newY].isRoomEntrance):
        print(map[newX][newY].roomDescription)
    elif (map[newX][newY].hasLockedDoor):
        if (person.holdingKey == True):
            print("You opened the locked door and went through!")
        else:
            print("The door is locked! You cannot go through. Maybe a key would help?")
            if (direction.lower() == ("north")):
                yPosition += 1
            if (direction.lower() == ("south")):
                yPosition -= 1
            if (direction.lower() == ("east")):
                xPosition -= 1
            if (direction.lower() == ("west")):
                xPosition += 1     
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
            if (direction.lower() == ("north")):
                yPosition += 1
            if (direction.lower() == ("south")):
                yPosition -= 1
            if (direction.lower() == ("east")):
                xPosition -= 1
            if (direction.lower() == ("west")):
                xPosition += 1        

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
                encounter(newX, newY, direction)
            else:
                print("You have successfully moved.")
        if (map[newX][newY].isValid == False):
            if (map[newX][newY].isPillar):
                print("You hit a pillar.")
            else:
                print("You hit a wall.")
    else: print ("You hit a wall.")
    
while(True):
    direction = input("What direction do you want to go? ")
    move(direction)
    print("The x position is " + str(xPosition) + " and the y position is " + str(yPosition) + ".")