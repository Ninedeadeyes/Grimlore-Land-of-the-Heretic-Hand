
import os

#map
dungeonMap1= [ 
               [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
               [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
               [" "," "," "," ","0","0","0","0","0","0","0","0","0"," "," "," "," "],
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


playerMap1=  [
              [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
              [" "," "," "," ","0","0","0","0","0","0","0","0","0"," "," "," "," "],
              [" "," "," "," ","0",".",".","0",".",".",".",".","0"," "," "," "," "],
              [" "," "," "," ","0",".",".",".",".","@",".","0","0"," "," "," "," "],
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
              [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
              [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]   
          
x = 9
y = 4


def displayMapAround(maps,x,y):
    for x in range(0,16):
        map_row=str(maps[x]).replace(',', '').replace("'"," ").replace("."," ").replace("0","#")
        print(map_row)  

def clear_screen():
    print("\033c", end="")   
    displayMapAround(playerMapChoice,x,y) 

os.system("mode con cols=150 lines=50")

#selecting a map
mapChoice = dungeonMap1
playerMapChoice= playerMap1

displayMapAround(playerMapChoice,x,y)

#initialising the players position
position = mapChoice[0][0]

print(mapChoice[y][x])
while position != "E":
    #displayMap(playerMapChoice)
    previousX = x
    previousY = y
    playerMapChoice[y][x] = "."
    movement = input("W,S,D,A,MAP").upper()

    if movement == "W":
        y = y-1
        position = mapChoice[y][x]
        playerMapChoice[y][x] = "@"
        

    if movement == "S":
        y = y+1
        position = mapChoice[y][x]
        playerMapChoice[y][x] = "@"
        

    if movement == "D":
        x = x+1
        position = mapChoice[y][x]
        playerMapChoice[y][x] = "@"
        

    if movement == "A":
        x = x-1
        position = mapChoice[y][x]
        playerMapChoice[y][x] = "@"


    position = mapChoice[y][x]
    playerMapChoice[y][x] = "@"
    clear_screen()
    
    if position == "0" or position == "1":
        playerMapChoice[y][x] = "0"
        x = previousX
        y = previousY
        playerMapChoice[y][x] = "@"
        clear_screen()
        print("You hit a wall, you stumble in the darkness back to your previous position...")

        



