
import os


#map
dungeonMap = [ [" "," "," "," ","0","0","0","0","0","0","0","0","0"," "," "," "," "],
               [" "," "," "," ","0",".",".","0",".",".",".",".","0"," "," "," "," "],
               [" "," "," "," ","0",".",".",".",".",".",".","0","0"," "," "," "," "],
               [" "," "," "," ","0",".",".",".",".",".",".",".","0"," "," "," "," "],
               [" "," "," "," ","0",".",".",".","0",".",".",".","0"," "," "," "," "],
               [" "," "," "," ","0",".",".","0",".",".",".",".","0"," "," "," "," "],
               [" "," "," "," ","0",".",".",".",".",".",".",".","0"," "," "," "," "],
               [" "," "," "," ","0",".",".",".",".",".",".",".","0"," "," "," "," "],
               [" "," "," "," ","0",".",".",".",".",".",".",".","0"," "," "," "," "],
               [" "," "," "," ","0",".",".",".",".",".",".",".","0"," "," "," "," "],
               [" "," "," "," ","0",".",".",".",".",".",".",".","0"," "," "," "," "],
               [" "," "," "," ","0","0","0","0","0","0","0","0","0"," "," "," "," "],
               [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]   


playerMap =  [[" "," "," "," ","0","0","0","0","0","0","0","0","0"," "," "," "," "],
              [" "," "," "," ","0",".",".","0",".",".",".",".","0"," "," "," "," "],
              [" "," "," "," ","0",".",".",".",".",".",".","0","0"," "," "," "," "],
              [" "," "," "," ","0",".",".",".",".",".",".",".","0"," "," "," "," "],
              [" "," "," "," ","0",".",".","S","0",".",".",".","0"," "," "," "," "],
              [" "," "," "," ","0",".",".","0",".",".",".",".","0"," "," "," "," "],
              [" "," "," "," ","0",".",".",".",".",".",".",".","0"," "," "," "," "],
              [" "," "," "," ","0",".",".",".",".",".",".",".","0"," "," "," "," "],
              [" "," "," "," ","0",".",".",".",".",".",".",".","0"," "," "," "," "],
              [" "," "," "," ","0",".",".",".",".",".",".",".","0"," "," "," "," "],
              [" "," "," "," ","0",".",".",".",".",".",".",".","0"," "," "," "," "],
              [" "," "," "," ","0","0","0","0","0","0","0","0","0"," "," "," "," "],
              [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]   
          



x = 7
y = 4

def displayMapAround(maps,x,y):
    for x in range(0,14):
        map_row=str(maps[x]).replace(',', '').replace("'"," ").replace("."," ").replace("0","#")
        print(map_row)  


os.system("mode con cols=150 lines=50")

#selecting a map
mapChoice = dungeonMap

displayMapAround(playerMap,x,y)

#initialising the players position
position = mapChoice[0][0]



print(mapChoice[y][x])
while position != "E":
    print("\033c", end="")
    displayMapAround(playerMap,x,y)
    #displayMap(playerMap)
    previousX = x
    previousY = y
    playerMap[y][x] = "."
    movement = input("W,S,D,A,MAP").upper()

    if movement == "W":
        y = y-1
        position = mapChoice[y][x]
        playerMap[y][x] = "S"
        

    if movement == "S":
        y = y+1
        position = mapChoice[y][x]
        playerMap[y][x] = "S"
        

    if movement == "D":
        x = x+1
        position = mapChoice[y][x]
        playerMap[y][x] = "S"
        

    if movement == "A":
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
        



