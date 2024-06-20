import os
import random
from player import*
from functions import*
from dungeons import*
from settlements import*
from maps import*
from intro import Intro 
import winsound

gameloop=True

x=8
y=4


#FUNCTIONS 

def order(bag):
    for x in range(len(bag)): 
        print (x+1, str(bag[x]))

def displayMapAround(maps,x,y):
    for dy in (-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11):
        map_row = str(maps[y+dy][x-4:x+5]).replace(',', '').replace("'"," ").replace("."," ").replace("0","*")
        print(map_row)

def clear_screen_2():
    print("\033c", end="")     
    displayMapAround(playerMap,x,y)

#def clear_screen_1():
#    print("\033c", end="")        Defunct screen ( can show entire screen ) 
#    displayMap(playerMap)

#def displayMap(maps):    #Displaying the entire map
 #   for x in range(0,29):
  #      print(maps[x])

mapChoice =WorldMap


position = mapChoice[x][y]

hero=Player(100,0,10,5,0,0,0)

#INTRO

os.system("mode con cols=135 lines=49")

local_name=Intro()  # to import 'name' from intro

clear_screen_2()
print("                                                          ")
print("PRESS N + ENTER TO TURN MUSIC ON/OFF .")
print("                                                          ")


music=0
sound=0
cave=0           # trigger music for the Caves of Profound Misery
trigger=0        # trigger bg music for exiting Caves of Profound Misery

#( The trigger and cave variables prevents bg/rave music being restart everytime you go on the spaces and only when you are leaving or entering the cave)  


winsound.PlaySound(".\\music\\background.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)

#START OF GAME LOOP 

while gameloop == True:
    while True:
        previousX = x
        previousY = y
        playerMap[y][x] = (".")
        if position == ("~") and hero.ship==True:
            playerMap[y][x] = ("~")
        elif position ==("#") and hero.amulet==True:
            playerMap[y][x] = ("#")

        else:
            pass
            
        print("Name:",local_name," Health:",hero.health," STR:",(hero.strength+hero.weapon.damage)," Mana:",hero.mana," Gold:",hero.gold,)
        print("Class:",hero.player_class," XP:",hero.exp, " Level:",hero.level, " Talisman:",hero.talisman)
        print("Armour:",hero.armour.name,"+",hero.armour.protection," Weapon:",hero.weapon.name,"+",hero.weapon.damage)
        hero.turn_counter+=1
        hero.mana=min(hero.max_mana,hero.mana+1)
        movement=input("W,S,D,A,ITEMS(I),USE(U) Choice: ").upper()
      

#MOVEMENT

        if movement == "M":

            if music==0:
                y = y
                playerMap[y][x] = "@"
                clear_screen_2()
                print("Music change")
                winsound.PlaySound(".\\music\\bloodpit.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
                music=1
                break

            elif music==1:
                y = y
                playerMap[y][x] = "@"
                clear_screen_2()
                print("Music change")
                winsound.PlaySound(".\\music\\intro.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
                music=2
                break

            elif music==2:
                y = y
                playerMap[y][x] = "@"
                clear_screen_2()
                print("Music change")
                winsound.PlaySound(".\\music\\boss.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
                music=3
                break

            elif music==3:
                y = y
                playerMap[y][x] = "@"
                clear_screen_2()
                print("Music change")
                winsound.PlaySound(".\\music\\rave.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
                music=4
                break

            elif music==4:
                y = y
                playerMap[y][x] = "@"
                clear_screen_2()
                print("Music on")
                winsound.PlaySound(None,  winsound.SND_ALIAS)    
                winsound.PlaySound(".\\music\\background.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
                music=0
                break

        if movement == "N":

            if sound==0:
                y = y
                playerMap[y][x] = "@"
                clear_screen_2()
                print("Music off")
                winsound.PlaySound(None,  winsound.SND_ALIAS)
                sound=1
                break
            
            else:
                y = y
                playerMap[y][x] = "@"
                clear_screen_2()
                print("Music on")
                winsound.PlaySound(None,  winsound.SND_ALIAS)    
                winsound.PlaySound(".\\music\\background.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
                sound=0
                break
                


            
    
  
        if movement == "W":
            y = y-1
            position = mapChoice[y][x]
            playerMap[y][x] = "@"
            break

        elif movement == "S":
            y = y+1
            position = mapChoice[y][x]
            playerMap[y][x] = "@"
            break

        elif movement == "D":
            x = x+1
            position = mapChoice[y][x]
            playerMap[y][x] = "@"
            break

        elif movement == "A":
            x = x-1
            position = mapChoice[y][x]
            playerMap[y][x] = "@"
            break


        elif movement==("I"):
            playerMap[y][x] = "@"
            clear_screen_2()
            while True:
                print("Bag(B),Change(C),Spellbook(S), Exit(E)")
                choice=input("Choice: ").upper()
                clear_screen_2()


                if choice==("B"):
                    playerMap[y][x] = "@"
                    clear_screen_2()
                    print("Armour:",hero.armour.name," Weapon:",hero.weapon.name,"Gold:", hero.gold,"Diamond:",hero.diamond)
                    print("Healing potion:",hero.healing_potion,"Mana potion:",hero.mana_potion)
                    print("Demon Bone:", hero.demon_bone, "Ratling Fur:", hero.ratling_fur, "Imp Tooth:",hero.imp_tooth)
                    print("Demon Silk:",hero.demon_silk,"Iron Shard:",hero.iron_shard,"Brimstone:",hero.brimstone)
                    print ("")
                    order(hero.inventory)

                elif choice==("C"):
                    
                    while True:
                        playerMap[y][x] = "@"
                        clear_screen_2()
                        print("Weapon (W), Armour(A),Exit(E)")
                        choice=input("Choice: ").upper()
                         
                        if choice ==("W"):
                            playerMap[y][x] = "@"
                            clear_screen_2()
               
                            Weapons=[item for item in hero.inventory if isinstance (item,Weapon)]

                            if not Weapons:
                                print("You do not have any Weapon to equip")
                                break
                                
                            print (" Choose a Weapon to equip :")

                            for i,item in enumerate(Weapons,1):

                                print ("{}. {}".format(i,item))

                            valid=False
                            while not valid:
                                choice=input("")
                                try:
                                    bob=hero.weapon # fix bug that replicate item if error 
                                    hero.inventory.remove(Weapons[int(choice)-1])
                                    hero.weapon=Weapons[int(choice)-1]
                                    hero.inventory.append(bob)
                                    print("You arm yourself with :",Weapons[int(choice)-1])
                                    valid=True 

                                except (ValueError,IndexError):
                                    print("Invalid choice, try again ")
                            break 
                    

                        elif choice ==("A"):
                            playerMap[y][x] = "@"
                            clear_screen_2()
                        
               
                            Armours=[item for item in hero.inventory if isinstance (item,Armour)]

                            if not Armours:
                                print("You do not have any Armour to equip")
                                break
                                
                            print (" Choose a Armour to equip :")

                            for i,item in enumerate(Armours,1):

                                print ("{}. {}".format(i,item))

                            valid=False
                            while not valid:
                                choice=input("")
                                try:
                                    bob=hero.armour  # fix bug that replicate item if error 
                                    hero.inventory.remove(Armours[int(choice)-1])
                                    hero.armour=Armours[int(choice)-1]
                                    hero.inventory.append(bob)
                                    print("You equip yourself with:", Armours[int(choice)-1])
                                    valid=True 

                                except (ValueError,IndexError):
                                    print("Invalid choice, try again ")
                            break

                        elif choice ==("E"):
                            break


                        else:
                            print ("invalid choice")
                            


                elif choice==("S"):
                    playerMap[y][x] = "@"
                    clear_screen_2()
                    if hero.fire_bolt==True:
                        print("Fire Bolt: Dam : 70 to 120 Mana:4 INFO: Stun enemy for the round" )
                    else:
                        print ("Fire Bolt : ??????????????")

                    if hero.shadow_flee==True:
                        print("Shadow Flee: Dam :  None  Mana:2 INFO: 100% escape non-dungeon combat")
                    else:
                        print ("Shadow Flee : ??????????????")

                    if hero.divine_heal==True:
                        print("Divine Heal: Dam :  None  Mana:7/4(Holy Knight) INFO: Heal all damage ")
                    else:
                        print ("Divine Heal : ??????????????")

                    if hero.ice_blast==True:
                        print("Ice Blast: Dam : 60 to 100 Mana:5 INFO: Stun enemy, allowing 2 extra melee attacks ")
                    else:
                        print ("Ice Blast : ??????????????")

                    if hero.chaos_vortex==True:
                        print("Chaos Vortex: Dam : 200 to 500 Mana:6 INFO: Stun enemy but inflicts between 5 to 40 damage, self damage ")
                    else:
                        print ("Chaos Vortex : ??????????????")


                elif choice==("E"):
                    break
                    

                else:
                    print("invalid choice")
                    clear_screen_2()
  

        elif movement==("U"):
            
            while True:
                print ("What would you like to use ? Healing Potion +250 Hp(H), Mana Potion +25 Mana(M), Exit(E)")
                choice=input("Use:").upper()
                playerMap[y][x] = "@"
                clear_screen_2()

                
                
                if choice==("H"):
                
                    if hero.healing_potion>0:
                        hero.healing_potion-=1
                        heal=250
                        hero.health=min(hero.max_health,hero.health+heal)
                        print( "you drink a healing potion")
                        print("Your health is", str(hero.health))
                        input("Press any key to continue")
                        playerMap[y][x] = "@"
                        clear_screen_2()

                        break
                    else:
                        print("you have no more healing potion")
                        input("Press any key to continue")
                        playerMap[y][x] = "@"
                        clear_screen_2()
                        break


                elif choice==("M"):
                
                    if hero.mana_potion>0:
                        hero.mana_potion-=1
                        recharge=25
                        hero.mana=min(hero.max_mana,hero.mana+recharge)
                        print( "you drink a mana potion")
                        print("Your mana is", str(hero.mana))
                        input("Press any key to continue")
                        playerMap[y][x] = "@"
                        clear_screen_2()          
                        break
                    
                    else:
                        print("you have no more mana potion")
                        input("Press any key to continue")
                        playerMap[y][x] = "@"
                        clear_screen_2()
                        break

                elif choice==("E"):
                    
                    input("Press any key to continue")
                    playerMap[y][x] = "@"
                    clear_screen_2()    
                    break

                else:
                    print("invalid option")
                    input("Press any key to continue")
                    playerMap[y][x] = "@"
                    clear_screen_2()    


        else:
            position = mapChoice[y][x]
            playerMap[y][x] = "@"
            clear_screen_2()
            print("Invalid choice")
            print("              ")
#POSITION

    if position == ".":
        playerMap[y][x] = "@"
        clear_screen_2()

        if hero.map==True:    # reduce amount of random battles outside of introduction area 
        
            r=random.random()
            if r < 0.95 :
                nothing()
                print("                 ")

            elif r < 0.80:
                battle_2(hero)
                clear_screen_2()
                             
            else:
                hero.gold+=treasure()   
                print("                 ")

        else:

            r=random.random()
            if r < 0.85 :
                nothing()
                print("                 ")
                

            elif r < 0.95:
                battle_1(hero)
                clear_screen_2()
                             
            else:
                hero.gold+=treasure()   # From functions, i like how the coding mechanic works, so kept it like this
                print("                 ")
            

    elif position == "/":
        playerMap[y][x] = "@"
        clear_screen_2()

        r=random.random()

                
        if r < 0.80 :
            nothing()
            print("                 ")
            

        elif r < 0.95:
            battle_3(hero)
            clear_screen_2()
                         
        else:
            hero.gold+=treasure()   # From functions, i like how the coding mechanic works, so kept it like this
            print("                 ")

    elif position =="y":
        playerMap[y][x] = "@"
        clear_screen_2()
        if cave==1:
            winsound.PlaySound(".\\music\\rave.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
            cave=0
            trigger=1
        print("You feel something different..")
        print("                                          ")   
             


    elif position =="Y":
        playerMap[y][x] = "@"
        clear_screen_2()
        if trigger==1:
            winsound.PlaySound(".\\music\\background.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
            trigger=0
        cave=1
        print("You see a wooden sign, it reads")
        print("WARNING:You are about to enter the Caves of Profound Misery")
        print("Monsters are incredibly dangerous in here")
        print("                                          ")   

    elif position == "0": 
        playerMap[y][x] = "0"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        print("You are at a wall and you cannot pass.")
        print("                                      ")

    elif position == "~":
        if hero.ship==False:
            playerMap[y][x] = "~"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen_2()
            print("You cannot walk on water ")
            print("                                      ")
        else:
            playerMap[y][x] = "@"
            clear_screen_2()
            print("You sail pass in your ship")
            print("                                      ")

    elif position == "#":
        if hero.amulet==False:
            playerMap[y][x] = "#"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen_2()
            print("You cannot pass the bed of souls.. The darkness is too great")
            print("                                      ")
        else:
            playerMap[y][x] = "@"
            clear_screen_2()
            print("You walk through the bed of souls, with amulet in hand")
            print("                                      ")


    elif position=="?":
        playerMap[y][x] = "@"
        clear_screen_2()
        print("You stumble upon a secret door")
        print("                                      ")
        

    
    elif position == "!":
        if hero.marks==False:
            playerMap[y][x] = "0"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen_2()
            print("You cannot pass though here these rocky terrains.")
            print("                                      ")
        else:
            playerMap[y][x] = "@"
            clear_screen_2()
            print("You found a secret passageway, you journey ahead")
            print("                                      ")

    elif position == "R":
            playerMap[y][x] = "R"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen_2()
            rag_man_1(hero)
            print("                                                        ")
            clear_screen_2()

    elif position == "r":
            playerMap[y][x] = "R"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen_2()
            rag_man_2(hero)
            print("                                                        ")
            clear_screen_2()

    elif position == "r":
            playerMap[y][x] = "R"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen_2()
            rag_man_2(hero)
            print("                                                        ")
            clear_screen_2()

    elif position == "J":
            playerMap[y][x] = "O"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen_2()
            abandoned_outpost(hero)
            print("                                                        ")
            clear_screen_2()



    elif position=="9":
        playerMap[y][x] = "@"
        clear_screen_2()
        if hero.diamond_1==False:
            diamond(hero)
            hero.diamond_1=True
        else:
            nothing()

    elif position=="8":
        playerMap[y][x] = "@"
        clear_screen_2()
        if hero.diamond_2==False:
            diamond(hero)
            hero.diamond_2=True
        else:
            nothing()

    elif position=="Q":
        playerMap[y][x] = "@"
        clear_screen_2()
        if hero.diamond_3==False:
            diamond(hero)
            hero.diamond_3=True
        else:
            nothing()

    elif position=="D":
        playerMap[y][x] = "@"
        clear_screen_2()
        if hero.diamond_4==False:
            diamond(hero)
            hero.diamond_4=True
        else:
            nothing()

    elif position=="E":
        playerMap[y][x] = "@"
        clear_screen_2()
        if hero.diamond_5==False:
            diamond(hero)
            hero.diamond_5=True
        else:
            nothing()

 
#QUEST
    elif position == "C":
        if hero.sidequest_2==True and hero.sideboss_2_alive==True:
            playerMap[y][x] = "C"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen_2()
            outside_sideboss_2(hero)
            print("                                                        ")
            clear_screen_2()

        elif hero.sidequest_2==False and hero.sideboss_2_alive==True :
            playerMap[y][x] = "C"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen_2()
            print("You see some strange caves, you have a bad feeling")
            print("There are bones scattered across the floor ")
            print("The caves are not easy to navigate through without a map")
            print("Maybe someone at a settlement might be able to help...")
            print("                                                        ")
        elif hero.map==False:
            playerMap[y][x] = "C"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen_2()
            print("Even though you have killed the Sea Beast")
            print("You cannot navigate through these caves without a map")
            print("Go back to the settlement to collect your reward")
            print("                                                        ")

        elif hero.map==True:
            playerMap[y][x] = "@"
            clear_screen_2()
            print("The caves are no longer an issue for you with your map, you journey ahead")
            print("                                                        ")

    elif position == "K":
        if hero.doom_king_alive==True:
            playerMap[y][x] = "K"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen_2()
            doom_king(hero)
            print("                                                        ")
            clear_screen_2()

        else:
            playerMap[y][x] = "K"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen_2()
            print("The doom king bodies lay dead slaughtered by your violent hands")
            print("Nothing has changed much since his demise, maybe his death was not necessary ")
            input("Press enter to continue")
            clear_screen_2()
            
    elif position == "H":
        if hero.sidequest_3==True and hero.sideboss_3_alive==True and hero.sidequest_3_escape==False:
            playerMap[y][x] = "H"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen_2()
            outside_sideboss_3(hero)
            clear_screen_2()
            
        else:
            playerMap[y][x] = "H"
            x = previousX
            y = previousY
            playerMap[y][x] = "@"
            clear_screen_2()
            print("You see an empty bunk but nothing of value here")
            print("                                      ")


    elif position == "B":
        playerMap[y][x] = "B"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        blood_pit(hero)
        clear_screen_2()          

    elif position == "W":
        playerMap[y][x] = "W"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        outside_doom_wizard(hero)
        clear_screen_2()

    elif position == "G":
        playerMap[y][x] = "G"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        goblin_shaman(hero)
        clear_screen_2()


    elif position == "N":
        playerMap[y][x] = "N"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        outside_nine_dead_eyes(hero)
        clear_screen_2()    

#SETTLEMENT 

    elif position==("S"):
        playerMap[y][x] = "S"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        settlement_1(hero)
        playerMap[y][x] = "@"
        clear_screen_2()

    elif position==("A"):
        playerMap[y][x] = "S"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        settlement_2(hero)
        playerMap[y][x] = "@"
        clear_screen_2()

    elif position==("Z"):
        playerMap[y][x] = "S"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        settlement_3(hero)
        playerMap[y][x] = "@"
        clear_screen_2()

    elif position==("P"):
        playerMap[y][x] = "P"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        settlement_4(hero)
        playerMap[y][x] = "@"
        clear_screen_2()


    elif position==("X"):
        playerMap[y][x] = "S"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        settlement_5(hero)
        playerMap[y][x] = "@"
        clear_screen_2()  
         

#DUNGEONS 

    elif position==("1"):
        playerMap[y][x] = "T"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        while True:
            print ("Do you want to enter the Temple of Apshai?")
            print("You hear the Temple is not that dangerous ")
            print("Yes(Y), No(N)")
            choice=input("Choice:").upper()
            if choice==("Y"):
                dungeon_1(hero)
                clear_screen_2()
                break

            elif choice==("N"):
                print("You decide not to enter the Temple")
                clear_screen_2()
                break

            else:
                clear_screen_2()
                pass       
        

    elif position==("2"):
        playerMap[y][x] = "D"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        while True:
            print ("Do you want to enter the Dungeon of Doom?")
            print("You hear the dungeon is quite dangerous ")
            print("Yes(Y), No(N)")
            choice=input("Choice:").upper()
            if choice==("Y"):
                dungeon_2(hero)
                clear_screen_2()
                break

            elif choice==("N"):
                print("You decide not to enter the dungeon")
                clear_screen_2()
                break

            else:
                clear_screen_2()
                pass



    elif position==("3"):
        playerMap[y][x] = "D"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        while True:
            print ("Do you want to enter the Dungeon of Akalabeth?")
            print("You hear the dungeon is dangerous ")
            print("Yes(Y), No(N)")
            choice=input("Choice:").upper()
            if choice==("Y"):
                dungeon_3(hero)
                clear_screen_2()
                break

            elif choice==("N"):
                print("You decide not to enter the dungeon")
                clear_screen_2()
                break

            else:
                clear_screen_2()
                pass

    elif position==("4"):
        playerMap[y][x] = "D"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        while True:
            print ("Do you want to enter the Dungeon of Daggerfall?")
            print("You hear the dungeon is dangerous ")
            print("Yes(Y), No(N)")
            choice=input("Choice:").upper()
            if choice==("Y"):
                dungeon_4(hero)
                clear_screen_2()
                break

            elif choice==("N"):
                print("You decide not to enter the dungeon")
                clear_screen_2()
                break

            else:
                clear_screen_2()
                pass

    elif position==("5"):
        playerMap[y][x] = "T"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        while True:
            print ("Do you want to enter the Cultist Temple of lost souls?")
            print("You hear the Temple is quite dangerous ")
            print("Yes(Y), No(N)")
            choice=input("Choice:").upper()
            if choice==("Y"):
                dungeon_5(hero)
                clear_screen_2()
                break

            elif choice==("N"):
                print("You decide not to enter the dungeon")
                clear_screen_2()
                break

            else:
                clear_screen_2()
                pass           

  
    elif position==("6"):
        playerMap[y][x] = "D"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        while True:
            print ("Do you want to enter the Demonic Stronghold of Gahlak ")
            print("You hear the Dungeon is very dangerous ")
            print("Yes(Y), No(N)")
            choice=input("Choice:").upper()
            if choice==("Y"):
                dungeon_6(hero)
                clear_screen_2()
                break

            elif choice==("N"):
                print("You decide not to enter the dungeon")
                clear_screen_2()
                break

            else:
                clear_screen_2()
                pass           

    elif position==("7"):
        playerMap[y][x] = "T"
        x = previousX
        y = previousY
        playerMap[y][x] = "@"
        clear_screen_2()
        while True:
            print ("Do you want to enter the Temple of the Clockwork Fiend  ")
            print("You hear the Temple is very dangerous ")
            print("Yes(Y), No(N)")
            choice=input("Choice:").upper()
            if choice==("Y"):
                dungeon_7(hero)
                clear_screen_2()
                break

            elif choice==("N"):
                print("You decide not to enter the Temple")
                clear_screen_2()
                break

            else:
                clear_screen_2()
                pass           
