# test = input("Input something: ")
# print(test)
maxX = 3
maxY = 3
xPosition = 0
yPosition = 0

class Tile:
    isValid = False
    hasEncounter = False

map = [[Tile() for j in range(maxY)] for i in range(maxX)]
map[0][0].isValid = True
map[0][1].isValid = True
map[0][1].hasEncounter = True

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
        else: print("You hit a wall.")
    else: print ("You hit a wall.")

def encounter():
    print("hi")
    
    
while(True):
    direction = input("What direction do you want to go?")
    move(direction)

