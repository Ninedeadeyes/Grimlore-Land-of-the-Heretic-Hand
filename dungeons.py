import random
from player import Player
from animation import dungeon_art,temple_art
import time 

game=("poker","dice","mahjong","bingo","rummy","roulette")

#1ST DUNGEON 

def dungeon_print():
    print("\033c", end="")
    dungeon_art()
    print("loading...")
    time.sleep(.5)
    print("\033c", end="")
    dungeon_art()
    print("loading..")
    time.sleep(.5)
    print("\033c", end="")
    dungeon_art()
    print("loading.")
    time.sleep(.5)
    print("\033c", end="")
    dungeon_art()
    print("loading")
    time.sleep(.5)
    print("\033c", end="")

    
def temple_print():
    print("\033c", end="")
    temple_art()
    print("loading...")
    time.sleep(.5)
    print("\033c", end="")
    temple_art()
    print("loading..")
    time.sleep(.5)
    print("\033c", end="")
    temple_art()
    print("loading.")
    time.sleep(.5)
    print("\033c", end="")
    temple_art()
    print("loading")
    time.sleep(.5)
    print("\033c", end="")

def tresure_chest_1(Player):
    while True:
        print ("You stumble upon a treasure chest")
        choice=input("Do you open the chest? Yes (Y), No(N)").upper()

        if choice==("Y"):
            r=random.random()
            if r<.50:
                Player.gold+=50
                print("You have found 50 gold coins")
                input("Press any key to continue")
                break

            else:
                print("Alas, it was a Mimic !! ")
                Player.enemy("Mimic",8,100,60,50,"nothing")
                break
        else:
            print("You decide to leave the chest alone")
            break

def tresure_chest_2(Player):
    while True:
        print ("You stumble upon a treasure chest")
        choice=input("Do you open the chest? Yes (Y), No(N)").upper()

        if choice==("Y"):
            r=random.random()
            if r<.50:
                Player.gold+=200
                print("You have found 200 gold coins")
                input("Press any key to continue")
                break

            else:
                print("Alas, it was a Greater Mimic !! ")
                Player.enemy("Greater Mimic",30,250,350,50,"nothing")                    
                break
        else:
            print("You decide to leave the chest alone")
            break

def tresure_chest_3(Player):
    while True:
        print ("You stumble upon a treasure chest")
        choice=input("Do you open the chest? Yes (Y), No(N)").upper()

        if choice==("Y"):
            r=random.random()
            if r<.50:
                Player.gold+=1000
                print("You have found 1000 gold coin")
                input("Press any key to continue")
                break

            else:
                print("Alas, it was a Demonic Mimic !! ")
                Player.enemy("Demonic Mimic",60,250,500,1000,"nothing")
                break
        else:
            print("You decide to leave the chest alone")
            break

def goblin_gamble(Player):
    while True:
        print("You stumble upon a goblin who invite you for a gamble")
        choice=input("Do you accept the offer? Yes (Y), No(N)").upper()
 
        if choice==("Y" or "YES"):
            game_type=random.choice(game)
            print("The goblin decide it will be a game of",game_type)
            while True:
                bet=input("how much do you bet?")
                try:
                    int(bet)
                    break
                except:
                    print("This is not a number")
                    
            while int(bet)>Player.gold:
                print("\033c", end="")
                print("You do not have enough gold. Please try again")
                while True:
                    bet=input("how much do you bet?")
                    try:
                        int(bet)
                        break
                    except:
                        print("This is not a number")

            bet=int(bet)
            guess=random.randint(1,3)
            die_1=random.randint(1,3)

            if die_1!=guess:
                print("The goblin has bested you in the game of",game_type)
                print("You lose",str(bet),"gold")
                Player.gold-=bet

            else:
                print("You have bested the goblin in the game of",game_type)
                win=bet*2
                print("You win",str(win),"gold")
                Player.gold+=bet
        else:
            print("You decide not to gamble your gold")

        input("Press enter to continue")
            
        break

    
                
            
                
            


def dungeon_1 (Player):
    while True:
        temple_print()
        dungeon_battle_1(Player)
        print("\033c", end="")
        dungeon_battle_1(Player)
        print("\033c", end="")
        print("You find a way out of the temple")
        choice=input("Escape(E) or Remain(R)").upper()
        if choice ==("E"):
            input("Press Enter to leave the temple")
            Player.dungeon=False
            print("\033c", end="")
            break
        elif choice ==("R"):
            print("You decide to move ahead against the undying darkness")
        else:
            print("Invalid choice, but it is too late to make a decision")
            print("A horde of monsters has blocked the exit")
        input("Press enter to continue")
        print("\033c", end="")
        dungeon_battle_1(Player)
        print("\033c", end="")
        dungeon_battle_1(Player)
        print("\033c", end="")
        print("In the corner of your eye you spot something.. ")
        r= random.random()
        if r <.60:
            print("You find a Treasure Chest!!")
            print("You gain 100 gold")
            Player.gold+=100
            
        elif r<.50:
            print("You find a Demon Bone")
            Player.demon_bone+=1

        elif r<.90:
            print("You find a Brimstone")
            Player.brimstone+=1

        else:
            print("You find a Iron Shard")
            Player.iron_shard+=1
            
            

        Player.dungeon=False
        Player.reputation+=2
        print("You gain 2 reputations")
        input("Press Enter to leave the temple")
        print("\033c", end="")
        break


def dungeon_battle_1(Player):
    print("deeper into the temple you go")
    Player.dungeon=True
       
    r= random.random()
    if r < .50:
        print("A Ratling sneaks up behind you ")
        Player.enemy("Ratling",2,80,30,30,"Ratling Fur")   

    elif r <.80:
        print ("You see a Lesser Demon ready to feed")
        Player.enemy("Lesser Demon",4,100,40,35,"Demon Bone")   
        

    elif r < .90:
        print("From the depth of darkness, a Brimstone Gremlin attacks ")
        Player.enemy("Brimstone Gremlin",6,100,50,40,"Brimstone")

    elif r <.50:
        tresure_chest_1(Player)

    else:
        goblin_gamble(Player)
            


#2ND DUNGEON 

def dungeon_2 (Player):
    while True:
        dungeon_print()
        dungeon_battle_2(Player)
        print("\033c", end="")
        dungeon_battle_2(Player)
        print("\033c", end="")
        dungeon_battle_2(Player)
        print("\033c", end="")
        print("You find a way out of the dungeon")
        choice=input("Escape(E) or Remain(R)").upper()
        if choice ==("E"):
            input("Press Enter to leave the dungeon")
            Player.dungeon=False
            print("\033c", end="")
            break
        elif choice ==("R"):
            print("You decide to move forward")
        else:
            print("Invalid choice, but it is too late to make a decision")
            print("A horde of monsters has blocked the exit")
        input("Press enter to continue")
        print("\033c", end="")
        dungeon_battle_2(Player)
        print("\033c", end="")
        dungeon_battle_2(Player)
        print("\033c", end="")    
        dungeon_battle_2(Player)
        print("\033c", end="")
        if Player.sidequest_1==True and Player.sideboss_1_alive==True:
            dungeon_sideboss_1(Player)
        else:
            pass
        
        print("You have cleared the dungeon for now ")
        print("In the corner of your eye you spot something.. ")
        r= random.random()
        if r <.80:
            print("You find a Treasure Chest!!")
            print("You gain 200 gold")
            Player.gold+=200
            
        elif r<90:
            print("You find a healing potion")
            Player.healing_potion+=1                  
            
        else:
            print("You find a Iron Shard")
            Player.iron_shard+=1
            

        Player.dungeon=False
        Player.reputation+=5
        print("You gain 5 reputation")
        input("Press any key to leave the dungeon")
        print("\033c", end="")
        break


def dungeon_battle_2(Player):
    
    Player.dungeon=True
    print("deeper into the dungeon you go")   
    r= random.random()
    if r < .30:
        print("From the depth of darkness, a Brimstone Gremlin attacks ")
        Player.enemy("Brimstone Gremlin",6,100,50,40,"Brimstone")

    elif r <.40:
        print("The dead wakes from his slumber, a Fallen Knight rises ")
        Player.enemy("Fallen Knight",8,160,80,50,"Iron Shard") 
        

    elif r < .90:
        print(" You stumble upon a lone Ettercap. He wants to play with your guts ")
        Player.enemy("Ettercap",12,100,100,60,"Demon Silk")

    elif r <.50:
        tresure_chest_1(Player)

    else:
        goblin_gamble(Player)
            
            


def dungeon_sideboss_1(Player):
        
        Player.dungeon=True
        print("You see Balgot, the Demon Troll, prepare for the fight of your life")
        Player.enemy("Demon Troll",15,200,120,60,"Demon Bone")
        print("You defeat the dreaded Demon Troll, now go and collect your bounty")
        Player.sideboss_1_alive=False


#3RD DUNGEON
        

def dungeon_3 (Player):
    while True:
        dungeon_print()
        dungeon_battle_3(Player)
        print("\033c", end="")
        dungeon_battle_3(Player)
        print("\033c", end="")
        dungeon_battle_3(Player)
        print("\033c", end="")
        print("You find a way out of the dungeon")
        choice=input("Escape(E) or Remain(R)").upper()
        if choice ==("E"):
            input("Press any key to leave the dungeon")
            Player.dungeon=False
            print("\033c", end="")
            break
        elif choice ==("R"):
            print("You decide to push ahead")
        else:
            print("Invalid choice, but it is too late to make a decision")
            print("A horde of monsters has blocked the exit")
        input("Press enter to continue")
        print("\033c", end="")
        dungeon_battle_3(Player)
        print("\033c", end="")
        dungeon_battle_3(Player)
        print("\033c", end="")
        dungeon_battle_3(Player)
        print("\033c", end="")

        if Player.sidequest_1==True and Player.sideboss_1_alive==True:
            dungeon_sideboss_1(Player)

        else:
            pass
        
        print("You have cleared the dungeon for now ")
        print("In the corner of your eye you spot something.. ")
        r= random.random()
        if r <.80:
            print("You find a Treasure Chest!!")
            print("You gain 300 gold")
            Player.gold+=300
            
        elif r<90:
            print("You find a healing potion")
            Player.healing_potion+=1                  
            
        else:
            print("You find a Iron Shard")
            Player.iron_shard+=1
            

        Player.dungeon=False
        Player.reputation+=10
        print("You gain 10 reputations")
        input("Press any key to leave the dungeon")
        print("\033c", end="")
        break


def dungeon_battle_3(Player):
    
    Player.dungeon=True
    print("deeper into the dungeon you go")   
    r= random.random()
    if r < .45:
        print(" You stumble upon a Chaos Spider. The Spider attacks you on sight ")
        Player.enemy("Chaos Spider",17,150,200,90,"Demon Silk")

    elif r <.60:
        print(" a Hellhound has marked your scent. Defend with violence")
        Player.enemy("Hellhound",20,180,250,120,"Demon Bone")
        

    elif r < .60:
        print("You hear a roar in the distance. A Iron Tusk Demon appears ")
        Player.enemy("Iron Tusk Demon",18,350,300,150,"Iron Shard") 
        

    elif r <.50:
        tresure_chest_2(Player)

    else:
        goblin_gamble(Player)


def dungeon_4 (Player):
    while True:
        dungeon_print()
        dungeon_battle_4(Player)
        print("\033c", end="")
        dungeon_battle_4(Player)
        print("\033c", end="")
        dungeon_battle_4(Player)
        print("\033c", end="")
        print("You find a way out of the dungeon")
        choice=input("Escape(E) or Remain(R)").upper()
        if choice ==("E"):
            input("Press any key to leave the dungeon")
            Player.dungeon=False
            print("\033c", end="")
            break
        elif choice ==("R"):
            print("\033c", end="")
            print("You decide to push ahead, against the darkness")
        else:
            print("\033c", end="")
            print("Invalid choice, but it is too late to make a decision")
            print("A horde of monsters has blocked the exit")
            print("deeper into the dungeon you go")
        input("Press enter to continue")
        print("\033c", end="")
        dungeon_battle_4(Player)
        print("\033c", end="")
        dungeon_battle_4(Player)
        print("\033c", end="")
        dungeon_battle_4(Player)
        print("\033c", end="")

        if Player.sidequest_1==True and Player.sideboss_1_alive==True:
            dungeon_sideboss_1(Player)

        else:
            pass
        
        print("You have cleared the dungeon for now ")
        print("In the corner of your eye you spot something.. ")
        r= random.random()
        if r <.80:
            print("You find a Treasure Chest!!")
            print("You gain 300 gold")
            Player.gold+=300
            
        elif r<90:
            print("You find a healing potion")
            Player.healing_potion+=1                  
            
        else:
            print("You find a Iron Shard")
            Player.iron_shard+=1
            

        Player.dungeon=False
        Player.reputation+=10
        print("You gain 10 reputations")
        input("Press any key to leave the dungeon")
        print("\033c", end="")
        break


def dungeon_battle_4(Player):
    
    Player.dungeon=True
    print("deeper into the dungeon you go")   
    r= random.random()
    if r < .40:
        print("You hear a rumbling in the distance. A Corrupted Iron Golem appears ")
        Player.enemy("Corrupted Iron Golem ",15,400,250,120,"Iron Shard") 

    elif r <.60:
        print(" A Ratling Assassin attacks you in the darkness. Fight for your life")
        Player.enemy("Ratling Assassin ",25,150,250,150,"Ratling Fur")
        

    elif r < .50:
        print(" You see a manical Demonic Abomination. End the wretched beast")
        Player.enemy("Demonic Abomination",22,250,300,200,"Demon Bone")

    elif r <.40:
        tresure_chest_2(Player)

    else:
        goblin_gamble(Player)

def dungeon_5 (Player):
    while True:
        temple_print()
        dungeon_battle_5(Player)
        print("\033c", end="")
        dungeon_battle_5(Player)
        print("\033c", end="")
        print("You find a way out of the temple")
        choice=input("Escape(E) or Remain(R)").upper()
        if choice ==("E"):
            input("Press any key to leave the temple ")
            Player.dungeon=False
            print("\033c", end="")
            break
        elif choice ==("R"):
            print("\033c", end="")
            print("You decide to push ahead against the undying darkness")
        else:
            print("\033c", end="")
            print("Invalid choice, but it is too late to make a decision")
            print("A horde of monsters has blocked the exit")
        input("Press enter to continue")
        print("\033c", end="")
        dungeon_battle_5(Player)
        print("\033c", end="")
        dungeon_battle_5(Player)
        print("\033c", end="")
        print("You find a way out of the temple")
        choice=input("Escape(E) or Remain(R)").upper()
        if choice ==("E"):
            input("Press any Enter to leave the temple")
            Player.dungeon=False
            print("\033c", end="")
            break
        elif choice ==("R"):
            print("\033c", end="")
            print("You decide to push ahead against the undying darkness")
        else:
            print("\033c", end="")
            print("Invalid choice, but it is too late to make a decision")
            print("A horde of monsters has blocked the exit")
        input("Press enter to continue")
        print("\033c", end="")            
        dungeon_battle_5(Player)
        print("\033c", end="")
        dungeon_battle_5(Player)
        print("\033c", end="")
        if Player.sidequest_5==True and Player.sideboss_5_alive==True:
            dungeon_sideboss_5(Player)
        else:
            pass
        print("You have cleared the temple for now ")
        print("In the corner of your eye you spot something.. ")
        r= random.random()
        if r <.80:
            print("You find a Treasure Chest!!")
            print("You gain 200 gold")
            Player.gold+=200
            
        elif r<90:
            print("You find a healing potion")
            Player.healing_potion+=1                  
            
        else:
            print("You find a Demon Bone")
            Player.demon_bone+=1
            

        Player.dungeon=False
        Player.reputation+=10
        print("You gain 10 reputations")
        input("Press any key to leave the dungeon")
        print("\033c", end="")
        break


def dungeon_battle_5(Player):
    print("deeper into the temple you go")
    Player.dungeon=True
       
    r= random.random()
    if r < .40:
        print("You hear the muttering of the insane. An Lunatic Cultist appears ")
        Player.enemy("Lunatic Cultist",14,180,150,80,"Brimstone") 

    elif r <.60:
        print(" You see a Chaos Spawn in your distance. Prepare for combat")
        Player.enemy("Chaos Spawn ",16,150,150,100,"Brimstone")
        

    elif r < .30:
        print(" A Cultist Champion rush towards you. Defend with violence")
        Player.enemy("Cultist Champion",20,250,300,200,"Demon Bone")

    elif r <.40:
        tresure_chest_2(Player)

    else:
        goblin_gamble(Player)


def dungeon_sideboss_5(Player):
        
        Player.dungeon=True
        print("You see Idijheh, the Cultist Impaler, prepare for the fight of your life")
        Player.enemy("Cultist Impaler,",30,400,400,400,"Demon Bone")
        print("You defeat the dreaded Cultist Impaler, now go and collect your reward")
        Player.sideboss_5_alive=False


def dungeon_6 (Player):
    while True:
        dungeon_print()
        dungeon_battle_6(Player)
        print("\033c", end="")
        dungeon_battle_6(Player)
        print("\033c", end="")
        print("You find a way out of the dungeon")
        choice=input("Escape(E) or Remain(R)").upper()
        if choice ==("E"):
            input("Press any key to leave the dungeon")
            Player.dungeon=False
            print("\033c", end="")
            break
        elif choice ==("R"):
            print("\033c", end="")
            print("You decide to push ahead, against the darkness")
        else:
            print("\033c", end="")
            print("Invalid choice, but it is too late to make a decision")
            print("A horde of monsters has blocked the exit")
            print("deeper into the dungeon you go")
        input("Press enter to continue")
        print("\033c", end="")  
        dungeon_battle_6(Player)
        print("\033c", end="")
        dungeon_battle_6(Player)
        print("\033c", end="")
        print("You find a way out of the dungeon")
        choice=input("Escape(E) or Remain(R)").upper()
        if choice ==("E"):
            input("Press any key to leave the dungeon")
            Player.dungeon=False
            print("\033c", end="")
            break
        elif choice ==("R"):
            print("\033c", end="")
            print("You decide to push ahead, against the darkness")
        else:
            print("\033c", end="")
            print("Invalid choice, but it is too late to make a decision")
            print("A horde of monsters has blocked the exit")
            print("deeper into the dungeon you go")
        input("Press enter to continue")
        print("\033c", end="")  
        dungeon_battle_6(Player)
        print("\033c", end="")
        dungeon_battle_6(Player)
        print("\033c", end="")
        dungeon_battle_6(Player)
        print("\033c", end="")
        dungeon_battle_6(Player)
        print("\033c", end="")
        print("You have cleared the dungeon for now ")
        print("In the corner of your eye you spot something.. ")
        r= random.random()
        if r <.80:
            print("You find a large stash of Demon Bones!!")
            print("You gain 5 Demon Bones ")
            Player.demon_bone+=5
            
        elif r<90:
            print("You find a large stash of gold")
            print("You gain 1000g ")
            Player.gold+=1000                  
            
        else:
            print("You find a small stash of Iron Shards")
            print("You gain 2 Iron Shard ")
            Player.iron_shard+=2
            

        Player.dungeon=False
        Player.reputation+=30
        print("You gain 30 reputations")
        input("Press any key to leave the dungeon")
        print("\033c", end="")
        break


def dungeon_battle_6(Player):
    
    Player.dungeon=True
    print("deeper into the dungeon you go")   
    r= random.random()
    if r < .40:
        print("You hear a rumbling in the distance. A Greater Demon appears ")
        Player.enemy("Greater Demon",45,300,700,750,"Demon Bone") 

    elif r <.60:
        print(" A Plague Demon attacks you in the darkness. Fight for your life")
        Player.enemy("Plague Demon",35,400,400,750,"Demon Bone")
        
    elif r < .50:
        print(" You see a manical Demon War Champion. End the wretched demon")
        Player.enemy("Demon War Champion",50,450,1000,1000,"Demon Bone")

    elif r <.40:
        tresure_chest_3(Player)

    else:
        goblin_gamble(Player)


def dungeon_7 (Player):
    while True:
        temple_print()
        dungeon_battle_7(Player)
        print("\033c", end="")
        dungeon_battle_7(Player)
        print("\033c", end="")
        print("You find a way out of the temple")
        choice=input("Escape(E) or Remain(R)").upper()
        if choice ==("E"):
            input("Press any key to leave the dungeon")
            Player.dungeon=False
            print("\033c", end="")
            break
        elif choice ==("R"):
            print("\033c", end="")
            print("You decide to push ahead against the undying darkness")
        else:
            print("\033c", end="")
            print("Invalid choice, but it is too late to make a decision")
            print("A horde of monsters has blocked the exit")
        input("Press enter to continue")
        print("\033c", end="")
        dungeon_battle_7(Player)
        print("\033c", end="")
        dungeon_battle_7(Player)
        print("\033c", end="")
        print("You find a way out of the temple")
        choice=input("Escape(E) or Remain(R)").upper()
        if choice ==("E"):
            input("Press any Enter to leave the dungeon")
            Player.dungeon=False
            print("\033c", end="")
            break
        elif choice ==("R"):
            print("\033c", end="")
            print("You decide to push ahead against the undying darkness")
        else:
            print("\033c", end="")
            print("Invalid choice, but it is too late to make a decision")
            print("A horde of monsters has blocked the exit")
        input("Press enter to continue")
        print("\033c", end="")
        dungeon_battle_7(Player)
        print("\033c", end="")
        dungeon_battle_7(Player)
        print("\033c", end="")
        dungeon_battle_7(Player)
        print("\033c", end="")
        dungeon_battle_7(Player)
        print("\033c", end="")    
        print("You have cleared the temple for now ")
        print("In the corner of your eyes you spot something.. ")
        r= random.random()
        if r <.80:
            print("You find a large stash of Iron Shards!!")
            print("You gain 5 Iron Shards")
            Player.iron_shard+=5
            
        elif r<90:
            print("You find a large stash of gold")
            Player.gold+=1000                  
            
        else:
            print("You find a small stash of Demon Bones")
            print("You gain 2 Demon Bones ")
            Player.demon_bone+=2

        Player.dungeon=False
        Player.reputation+=30
        print("You gain 30 reputations")
        input("Press any key to leave the dungeon")
        print("\033c", end="")
        break


def dungeon_battle_7(Player):
    print("deeper into the temple you go")
    Player.dungeon=True
       
    r= random.random()
    if r < .40:
        print("You hear the muttering of the insane. A Clockwork Horror appears ")
        Player.enemy("Clockwork Horror",65,150,600,750,"Iron Shard") 

    elif r <.50:
        print(" You see a Clockwork Pain Taker in your distance. Prepare for combat")
        Player.enemy("Clockwork Pain Taker  ",35,650,600,750,"Iron Shard")
        

    elif r < .80:
        print(" A Clockwork Engineer rush towards you. Defend with violence")
        Player.enemy("Clockwork Engineer",45,400,800,1000,"Iron Shard")

    elif r <.40:
        tresure_chest_3(Player)

    else:
        goblin_gamble(Player)

