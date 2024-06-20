import random
import time 
from player import Player
from data import nothing_list,weapon_list
from items import*
import winsound

def nothing():
    nothing=random.choice(nothing_list)
    print(nothing)

def battle_1(Player):
        
    r= random.random()
    if r < .50:
        print("From the shadows a Bog Imp attacks you ")
        Player.enemy("Bog Imp",1,80,20,25,"Imp Tooth")
        

    elif r < .80:
        print("A Ratling sneaks up behind you ")
        Player.enemy("Ratling",2,80,30,30,"Ratling Fur")   

    elif r<.90: 
        print ("You see a Lesser Demon ready to feed")
        Player.enemy("Lesser Demon",4,100,40,35,"Demon Bone")

def battle_2(Player):
        
    r= random.random()
    if r < .50:
        print("From the shadows a Hell Hound attacks you ")
        Player.enemy("Hell Hound",15,180,350,150,"Demon Bone")
        

    elif r < .80:
        print("A Ratling Death Stalker sneaks up behind you ")
        Player.enemy("Ratling Death Stalker",20,250,350,200,"Ratling Fur")   

    elif r<.90: 
        print ("You see a Red Ettercap ready to feed")
        Player.enemy("Red Ettercap",15,300,350,300,"Demon Silk")


def battle_3(Player):
        
    r= random.random()
    if r < .50:
        print("From the shadows a Doom Speaker attacks you ")
        Player.enemy("Doom Speaker",50,350,1000,1500,"Demon Silk")
        

    elif r < .80:
        print("A Hand of Ungas sneaks up behind you ")
        Player.enemy("Hand of Ungas",35,550,1000,1500,"Brimstone")   

    elif r<.90: 
        print ("You see a Death Bloom ready to feed")
        Player.enemy("Death Bloom",45,450,1200,2000,"Demon Silk")


def treasure():     #not needing an augement because 'return' was used. 
    gold=random.randint(1,6)
    print("you loot some dead bodies and find some gold. You find",str(gold),"gold")
    return gold

def diamond(Player):
    Player.diamond+=1
    print("Oh how lucky you found a Diamond on the floor")
    input("press Enter to continue ")

def rag_man_1(Player):
    while True: 
        print("You see a rag man who is buying Demon Silk")
        print("He will exchange 7x Demon Silk for a demonic weapon he found")
        choice=input("Yes(Y) NO(N)").upper()

        if choice==("Y"):
            if Player.demon_silk<7:
                print("You do not have enough demon silk")
                print("Come back another time")
                input("Press enter to continue")
                break
            else:
                Player.demon_silk-=7
                weapon=random.choice(weapon_list)
                print("You gain",weapon)
                print("With a sly smile the Rag man mutters 'lets do business again")
                Player.inventory.append(weapon)
                input("Press enter to continue")
                break 
        elif choice==("N"):
            print("Come back if you change your mind")
            input("Press enter to continue")
            break


        else:
            print("\033c", end="")
            print("I didn't quite catch that")
            

def rag_man_2(Player):
    while True: 
        print("You see a rag man who is buying Brimstone")
        print("He will exchange 7x Brimstone for a demonic weapon he found")
        choice=input("Yes(Y) NO(N)").upper()

        if choice==("Y"):
            if Player.brimstone<7:
                print("You do not have enough Brimstone")
                print("Come back another time")
                input("Press enter to continue")
                break
            else:
                Player.brimstone-=7
                weapon=random.choice(weapon_list)
                print("You gain",weapon)
                print("With a sly smile the Rag man mutters 'lets do business again")
                Player.inventory.append(weapon)
                input("Press enter to continue")
                break 
        elif choice==("N"):
            print("Come back if you change your mind")
            input("Press enter to continue")
            break


        else:
            print("\033c", end="")
            print("I didn't quite catch that")       
        
        
def abandoned_outpost(Player):
    while True:
        if Player.abandoned_outpost==False:
            print("You stumble upon an abandoned outpost")
            print("Will you search to see if there is anything useful?")
            choice=input("Yes(Y) NO(N)").upper()
            

            if choice==("Y"):
                Player.healing_potion+=5
                Player.mana_potion+=2
                Player.inventory.append(HereticPlateMail())
                Player.abandoned_outpost=True
                print("You find some magical potions and a Plate Mail Armour")
                print("You gain 5 x healing potions 2x mana potions and a Heretic Plate Mail")
                input("Press enter to continue")
                break

            elif choice==("N"):
                print("You decide to leave the outpost alone")
                input("Press enter to continue")
                break

            else:
                print("Invalid option")
                

        else:
            print("You have already ransacked the abandoned outpost")
            input("Press enter to continue")
            break

            
            
            
        
            
        
  

#OPEN WORLD QUEST

def outside_sideboss_2(Player):
        print("You scream out the name 'Atumbrath'and you hear a roar back")
        print("You see the Sea Beast prepare for the fight of your life")
        Player.enemy("Sea Beast",20,700,500,200,"Demon Bone")
        if Player.flee==True:
            print("\033c", end="")
            pass
        else:       
            print("\033c", end="")
            print("You defeat the dreaded Atumbrath, now go and collect your bounty")
            Player.sideboss_2_alive=False

def doom_king(Player):
        winsound.PlaySound(".\\music\\boss.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
        print("You see the Doom King on his throne. He speaks, 'A new challenger, how exciting' ")
        Player.enemy("Doom King",72,3000,10000,1000000,"Demon Bone")
        if Player.flee==True:
            winsound.PlaySound(".\\music\\background.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
            print("\033c", end="")
            pass
        else:       
            print("\033c", end="")
            winsound.PlaySound(".\\music\\ending.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
            print("You defeated the Doom King, you have freed the land from his evil hands")
            print("You have conquered the final boss, but can you find the 'true' ending ? " )
            print("You gain 1 million gold")
            print("You gain Doom King Plate Mail")
            print("You gain Doom King Sword")
            Player.inventory.append(DoomKingPlateMail())
            Player.inventory.append(DoomKingSword())
            print("                       ")
            input("Press enter to continue")
            winsound.PlaySound(".\\music\\background.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
            Player.doom_king_alive=False



def outside_sideboss_3(Player):
    print ("You have found the dreaded hideout of Nine Dead Eyes the Shadow Stalker")
    print ("You see that he is a human being. He looks back at you with a puzzled look and says")
    time.sleep(1.5)
    print("'You are aware the reason why they want me dead is because I beat them in a fair game of poker ?")
    print("It is true I took all their belongings but they knew the risk in gambling with old Nine Dead Eyes ")
    time.sleep(1.5)
    print("Surely that doesn't deserve the death penalty?") 
    print( "If you let me live I will teach you how to spot 'secrets' that even the keeniest eyes won't be able to see")
    while True:
        choice=input("Kill (K) Mercy (M)").upper()
        
        if choice==("M"):
            Player.marks=True
            Player.sidequest_3_escape=True 
            print("Nine Dead Eyes teaches you to look out for several 'marks' that indicate a secret door '")
            print(" and informs you how to open them. He wishes you well and abandon the hideout")
            input("Press enter to continue your adventure")
            break
              
        elif choice==("K"):
            print("I didn't want to do this but i must defend with violence")
            Player.enemy("Shadow Hunter",50,400,700,300,"nothing")

            if Player.flee==True:
                Player.sidequest_3_escape=True
                print("You escape the violent confrontation. I doubt that he will still be here next time")
                input("Press enter to continue your adventure")
                break

            else:
                Player.sideboss_3_alive=False
                print("You have slain Nine Dead Eyes in combat ")
                print("Go back to the Inn for your reward")
                input("Press enter to continue your adventure")
                break

        else:
           pass 
          
def outside_doom_wizard(Player):
    
    if Player.shadow_hunter==True or Player.holy_knight==True:
        print("You see a blind old man sitting on the floor, as you approach him he looks up and says")
        print("Buzz off, you mind has already been tainted by foul knowledge")
        input("Press enter key to continue your adventure")

    elif Player.doom_wizard==True:
        print("Hello young student, have you come to visit your master ?")
        input("Press enter key to continue your adventure")

    else:
        if Player.max_mana>19:
            print("You see a blind old man sitting on the floor, as you approch him he looks up and says")
            print("You have potential young one, I can feel the Mana flowing from you")
            print("I can teach you how to harness your full potential ? ")
            while True:
                
                choice=input("Yes(Y) or No(N)").upper()

                if choice==("Y"):
                    Player.doom_wizard=True
                    Player.player_class="Doom Wizard"
                    Player.max_mana+=12
                    print("After many months of training you become a deadly Doom Wizard  ")
                    print("You gain 12 max mana")
                    Player.mana=Player.max_mana
                    print("All spells are unlocked")
                    Player.fire_bolt=True
                    Player.shadow_flee=True
                    Player.ice_blast=True
                    Player.divine_heal=True
                    Player.chaos_vortex=True
                    input("Press enter to continue on your adventure")
                    break

                elif choice==("N"):
                    print("Have a think about it")
                    input("Press any key to continue on your adventure")
                    break
                    
                
                            
                
        else:
            print("You see a blind old man sitting on the floor, as you approch him he looks up and says")
            print("You have potential young one, come back when you are wiser ")
            print("Your need at least 20 Mana to upgrade CLASS to Doom Wizard")
            input("Press enter key to continue your adventure")
                            


def outside_nine_dead_eyes(Player):
    while True:
        if Player.sideboss_4_alive==True:
            print("You see a huge demon with a large meat cleaver")
            print("and in the corner 'Nine Dead Eyes in a very small cage")
            print("The huge demon approaches you with an evil grin and bellow's out  ")
            print("'Fresh meat for the lady tonight'")
            Player.enemy("Butcher",40,700,1000,500,"Demon Bone")
            if Player.flee==True:
                break
            else:
                Player.sideboss_4_alive=False
                print("You set Nine Dead Eyes free and he thanks you")

                if Player.doom_wizard==True or Player.holy_knight==True:
                    print ("He gives you a box of potions as a thank you")
                    print("he mutters 'You would have made a great student'")
                    print("'If you didn't pledge yourself to another master already'")
                    Player.healing_potion+=10
                    Player.mana_potion+=4
                    input("Press enter key to continue your adventure")
                    break

                else:
                    print("Thank you for saving me, the demon took me by surprise")
                    print("As a reward, I will teach you the ways of the Shadow Hunter")
                    choice=input("Yes (Y) No (N)").upper()
                    if choice==("Y"):
                        Player.shadow_hunter=True
                        Player.player_class="Shadow Hunter"
                        Player.max_strength+=15
                        Player.strength=Player.max_strength
                        Player.inventory.append(ShadowBlade())
                        print("After many months of training you become a Skilled Shadow Hunter")
                        print("Nine Dead Eyes gifts you with the Shadow Blade ")
                        print("As a reward for completing your training ")
                        print("You gain +15 to Max Strength")
                        print("You gain Shadow Blade")
                        print("You gain Passive Skill 'Master Killer' For every attack, you make an additional 'special attack' ")
                        print("You gain Passive Skill 'Be Quick or be Dead'. You gain an extra melee attack with Freeze Blast")
                        input("Press enter key to continue your adventure")
                        break

                    else:
                        print("Ok, come back if you do decide to become my student")
                        input("Press enter key to continue your adventure")
                        break 
                        
        else:
            if Player.doom_wizard==True or Player.holy_knight==True:
                print("Thank you for saving me")
                input("Press enter key to continue your adventure")
                break

            elif Player.shadow_hunter==True:
                print("Welcome back student")
                input("Press enter key to continue your adventure")
                break

            else:
                print("Have you decided to become my student?")

                choice=input("Yes(Y) No(N)").upper()

                if choice==("Y"):
                    Player.shadow_hunter=True
                    Player.player_class="Shadow Hunter"
                    Player.max_strength+=15
                    Player.strength=Player.max_strength
                    Player.inventory.append(ShadowBlade())
                    print("After many months of training you become a Skilled Shadow Hunter")
                    print("Nine Dead Eyes gifts you with the Shadow Blade ")
                    print("As a reward for completing your training ")
                    print("You gain +15 to Max Strength")
                    print("You gain Shadow Blade")
                    print("You gain Passive Skill 'Master Killer' For every attack, you make an additional 'special attack'  ")
                    print("You gain Passive Skill 'Be Quick or be Dead'. You gain an extra melee attack with Freeze Blast")
                    input("Press enter key to continue your adventure")
                    break

                else:
                    print("Ok, come back if you do decide to become my student")
                    input("Press enter key to continue your adventure")
                    break 
            

def goblin_shaman(Player):
    if Player.amulet==False:
        while True:
            print("You see a Goblin looking rather 'wise'. He whispers to you")
            print("'Hey you..I heard from someone you are looking to pass the bed of souls")
            print("I can sell you an Amulet that will help but I will need 10,000 gold, interested ?'")
            choice=input("Yes(Y) or No(N)").upper()

            if choice==("Y"):
                if Player.gold<10000:
                    print("You do not have enough gold")
                    input("Press enter to continue")
                    break
                else:
                    Player.gold-=10000
                    print("You have gain the Amulet of Ulgak Shield")
                    Player.inventory.append("Amulet of Ulgak Shield")
                    Player.amulet=True
                    input("Press enter to continue")
                    break

            elif choice==("N"):
                print("Come back if you change your mind")
                input("Press enter to continue")
                break

            else:
                print("I did not quite catch that")
                
    else:
        print("How nice of you to visit..I have no other gadgets that might be useful to you")
        input("Press enter to continue")
        
            
            
                        
def blood_pit( Player):
    Player.flee=False
    score=0
    while True:
        
        print("test your might and see how far you reach in the blood pit?")
        Choice=input("Do you want to enter? Y or N ").upper()

        if Choice==("Y"):
            winsound.PlaySound(".\\music\\bloodpit.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)
            print("Unlike within a dungeon you can escape a dual but it will reset the arena")
            print("There are 12 opponents")
            input("Press enter to continue")
            print("\033c", end="")
            while True:
                print("Your first Challenge arrives")
                Player.enemy("Demon Troll",15,200,120,60,"Demon Bone")
                if Player.flee==True:
                    break
                score+=1                
                print("\033c", end="")
                print("Next Challenger arrives")
                Player.enemy("Cultist Impaler,",30,300,400,600,"Demon Bone")
                if Player.flee==True:
                    break
                score+=1
                print("\033c", end="")
                print("Next Challenger arrives")
                Player.enemy("Greater Demon",40,250,700,750,"Demon Bone") 
                if Player.flee==True:
                    break
                score+=1
                print("\033c", end="")
                print("Next Challenger arrives")
                Player.enemy("Clockwork Horror",60,120,500,750,"Iron Shard")  

                if Player.flee==True:
                    break
                score+=1
                print("\033c", end="")
                print("Next Challenger arrives")                
                Player.enemy("Demon War Champion",45,400,1000,1000,"Demon Bone")
                if Player.flee==True:
                    break
                score+=1
                print("\033c", end="")
                print("Next Challenger arrives")
                Player.enemy("Hand of Ungas",35,550,1000,1500,"Brimstone")   
                if Player.flee==True:
                    break
                score+=1
                print("\033c", end="")
                print("Next Challenger arrives")   
                Player.enemy("Clockwork Pain Taker",30,600,1000,750,"Iron Shard")
                if Player.flee==True:
                    break
                score+=1
                print("\033c", end="")
                print("Next Challenger arrives")   
                Player.enemy("Doom Speaker",50,350,800,1500,"Demon Silk")
                if Player.flee==True:
                    break
                score+=1
                print("\033c", end="")
                print("Next Challenger arrives")   
                Player.enemy("Death Bloom",40,450,1200,2000,"Demon Silk")
                if Player.flee==True:
                    break
                score+=1
                print("\033c", end="")
                print("Next Challenger arrives")   
                Player.enemy("Black Dragon",65,600,1200,2000,"Demon Bone")
                if Player.flee==True:
                    break
                score+=1
                print("\033c", end="")
                print("Next Challenger arrives")   
                Player.enemy("Death Knight",70,550,1200,2000,"Demon Bone")
                if Player.flee==True:
                    break
                score+=1
                print("\033c", end="")
                print("Final Challenger arrives")  
                Player.enemy("Blood Pit Champion",78,1000,2000,2000,"nothing")
                if Player.flee==True:
                    break
                score+=1
                print("You have survived the arena ")
                input("Press enter to continue")
                break
            
            print("Your score was",score)
            winsound.PlaySound(".\\music\\background.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC +winsound.SND_LOOP)

            if score==12:
                print("You have defeated the arena")
                print("You have become the master of the pit !!")
                print("You gain 5 Diamonds ")
                print ("You gain 40 reputation")
                Player.diamond+=5
                Player.reputation+=40

            elif score >9 and score<12:
                print("That was a good show in the Blood Pit")
                print("Here is your payment for the grand display ")
                print("You gain 2 Diamonds ")
                Player.diamond+=2
                
                
            else:
                print("You are too weak for the pit, You don't deserve payment ")
                print("Come back when you are stronger")
                
            input("Press enter to continue ")
            break

        elif Choice==("N"):
            print("Ha chicken !!")
            break 

        else:
            print("\033c", end="")
            ("Invalid option ")
