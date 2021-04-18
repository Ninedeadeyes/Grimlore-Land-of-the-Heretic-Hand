import os
import msvcrt


#map
dungeonMap = [["0","0","0","0","0","0","0","0","0"],
              ["0",".",".","0",".",".",".",".","0"],
              ["0",".",".",".",".",".",".","0","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".","0",".",".",".","0"],
              ["0",".","0","0",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0","0","0","0","0","0","0","0","0"]]

playerMap  = [["0","0","0","0","0","0","0","0","0"],
              ["0",".",".","0",".",".",".",".","0"],
              ["0",".",".",".",".",".",".","0","0"],
              ["0","S",".",".",".",".",".",".","0"],
              ["0",".",".",".","0",".",".",".","0"],
              ["0",".","0","0",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0",".",".",".",".",".",".",".","0"],
              ["0","0","0","0","0","0","0","0","0"]]


x = 1
y = 3

def displayMapAround(maps,x,y):
  for dy in (-1,0,1):
    print( maps[y+dy][x-1:x+2] )



#Displaying the map
def displayMap(maps):
    for y in range(0,12):
        print(maps[y])

#selecting a map
mapChoice = dungeonMap

#initialising the players position
position = mapChoice[0][0]



print(mapChoice[y][x])
while position != "E":
    os.system('cls' if os.name == 'nt' else 'clear')
    displayMap(playerMap)
    previousX = x
    previousY = y
    playerMap[y][x] = "."
    print("W,S,D,A,MAP")
    movement = msvcrt.getch()

    if movement in {b'w', b'W'}:
        y = y-1
        position = mapChoice[y][x]
        playerMap[y][x] = "S"
        

    if movement in {b's', b'S'}:
        y = y+1
        position = mapChoice[y][x]
        playerMap[y][x] = "S"
        

    if movement in {b'd', b'D'}:
        x = x+1
        position = mapChoice[y][x]
        playerMap[y][x] = "S"
        

    if movement in {b'a', b'A'}:
        x = x-1
        position = mapChoice[y][x]
        playerMap[y][x] = "S"


    position = mapChoice[y][x]
    playerMap[y][x] = "S"
    
    if position == "0" or position == "1":
        print("You hit a wall, you stumble in the darkness back to your previous position...")
        playerMap[y][x] = "0"
        x = previousX
        y = previousY
        playerMap[y][x] = "S"
        



