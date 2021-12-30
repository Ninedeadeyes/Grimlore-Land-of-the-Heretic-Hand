import random
from player import Player
from items import*
from data import*
from maps import*

def print_settlement():
    print("\033c", end="")
    print("""                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                    hhhh            
                                                                                  hh    hh          
                                                                                yy        yy        
                                                                                MM        MM        
                                                                                  yy    yy         
yyyyyyyyyyyyyyyyyyyy              yyyyyyyyyy                                        yyyy           
++++++++++++++++++++ss          ss++++++++++ss                                                 
                    MM          MMssssssssssMM                                                      
  ssss  ssss  ssss  MM          MM++++++++++MM                                                      
  MMMM  MMMM  MMMM  MM          MM          MM                                                      
  oooo  oooo  oooo  MM          MM          MM                                                      
                    MM          MM          MM                                                      
                    MM          MM          MM                                                      
  ++++  ++++  ++++  MM          MM          MM                                                      
  MMMM  MMMM  MMMM  MM          MM          MM                                                      
  ssss  ssss  ssss  MM          MM          MM                                                      
                    MM          MM          MM++++++++++++++++                                      
              //////MM////////  MM          yyyyyyyyyyyyyyyyyy//      ////////////          ////////
            //yyyyyyyyyyyyyyyy//MM    //////        //////    MM    //yyyyyyyyyyyy//      //yyyyyyyy
            MM  ////    ////  MMMM    MMMMMM        MMMMMM    MM  //MM////////////MM//  //MM////////
            MM  MMMM    MMMM  MMMM    MMMMMM        MMMMMM    MM  yyMMyyyyyyyyyyyyMMyy  yyMMyyyyyyyy
            MM  hhhh    hhhh  MMMM    hhhhhh        hhhhhh    MM    MM            MM      MM        
::::        MM                MMMM                            MM    MM            MM      MM        
MMMM::      MM    ::::::      MMMM          ::::::::          MM    MM::::::::::::MM      MM::::::::
MMMMMM      MM    MMMMMM      MMMM          MMMMMMMM          MM    MMddddddddddddMM      MMdddddddd
MMMMMM      MM    MMMMMM      MMMM          MMMMMMMM          MM    MM            MM      MM        
MMMMMM------MM----MMMMMM------MMMM----------MMMMMMMM----------MM----MM------------MM------MM--------
dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                                                                                                                                                                                                                                                                                      
""")




def settlement_1(Player):

    while True :
        print("You stumble upon a small human settlement named 'Beggar's Hole'.")
        print("Gold:",Player.gold,"Health:",Player.health,"Healing potion:",Player.healing_potion,"Mana potion:",Player.mana_potion,"Reputation:",Player.reputation)
        print("                                                                 ")
        print("Inn(I),Temple(T),Blacksmith(B) Exit(E)")
        choice=input("Choice: ").upper()
        print_settlement()
        
        if choice==("I"):
            while True:
                print("What service would you like")
                print("Rest 30g (R),Drink/Gossip 1g (D), Blood Contract (B), Exit(E)" )
                choice=input("Choice:").upper()
                print_settlement()

                if choice==("R"):

                    if Player.gold<30:
                        print("You do not have enough gold to stay !!")

                    else:
                        Player.gold-=30
                        Player.health=Player.max_health
                        Player.mana=Player.max_mana
                        print("You wake up the next day ready for combat ")
                        print("Your health is",Player.health,"and your mana is",Player.mana)    
                        print("                             ")
                        
                elif choice==("D"):
                    if Player.gold<1:
                        print("You do not have enough gold for an Ale ")
                        print("                             ")
                    else:
                        Player.gold-=1
                        print("As you drink your Ale, you hear something helpful:")
                        tip=random.choice(tip_list_1)
                        print(tip)
                        print("                             ")

                elif choice==("B"):
                    if Player.sideboss_1_alive==True:                        
                        Player.sidequest_1=True
                        print("Defeat Balgot, the Demon Troll in the Dungeon of Doom. There is a bounty of 500g")
                        print("                             ")
                        
                    elif Player.sideboss_1_alive==False and Player.sidequest_1==True:
                        print("You have defeated Balgot the Demon Troll, here is your payment 500g ( You gain 50 reputation )")
                        print("                             ")       
                        Player.gold+=500
                        Player.reputation+=50
                        Player.sidequest_1=False
                    else:
                        print("Thank you for slaying the dreaded Demon Troll")
                        print("                             ")            
                elif choice==("E"):
                    break
                    
                else:
                    print("Sorry what was that again ?")


        elif choice==("T"):
            while True:
                print("What service would you like ?")
                print( "Buy Potions(P),Learn Spell (S) Exit(E)")
                choice=input("Choice:").upper()
                print_settlement()

                if choice==("P"):
                    print("What type of Potions would you like?")
                    print( "Healing Potion 350g (H), Mana Potion 500g(M)")
                    choice=input("Choice:").upper()     
                    print_settlement()

                    if choice==("H"):
                        if Player.gold<350:
                            print("You do not have enough gold")
                            print("                             ")


                        else:
                            Player.healing_potion+=1
                            Player.gold-=350
                            print( "You gain a healing potion")                            
                            print("                             ")

                    elif choice==("M"):

                        if Player.gold<500:
                            print("You do not have enough gold")
                            print("                             ")

                        else:
                            Player.mana_potion+=1
                            Player.gold-=500
                            print( "You gain a mana potion")
                            print("                             ")
                        
                    else:
                        print_settlement()
                        print("invalid choice")
                        print("                             ")
                
                elif choice==("S"):
                    print("What spell would you like to learn")
                    print("Fire Bolt 100g(F), Shadow Flee 50g(S)")
                    choice=input("Choice:").upper()     
                    print_settlement()
                    
                    if choice==("F"):

                        if Player.fire_bolt==(True):
                            print("You already know the spell")
                            print("                             ")

                        elif Player.gold<100:
                            print ("You do not have enough gold")
                            print("                             ")


                        else:
                            Player.fire_bolt=True
                            Player.gold-=100
                            print("You gain the ability to use fire bolt")
                            print("                             ")                

                    elif choice==("S"):
                        
                        if Player.shadow_flee==(True):
                            print("You already know the spell")
                            print("                             ")

                        elif Player.gold<50:

                            print ("You do not have enough gold")
                            print("                             ")
                            
                        else:
                            Player.shadow_flee=True
                            Player.gold-=50
                            print("You gain the ability to use Shadow Flee")
                            print("                             ")        

                    else:
                        print("invalid option")
                        print("                             ")

                elif choice==("E"):
                    break

                else:
                    print("invalid option")
                    print("                             ")            


        elif choice==("B"):
            while True: 
                print("What would you like to craft?")
                print("Ratskin Tunic-3 PROT, 1x Ratling fur and 75g                                (R)")
                print("Brimstone Bone Armour-12 PROT,2x Brimstone and 2x Demon Bone and 700 gold   (B)")
                print("Imp Tooth Spear-8 DAM, 1x Imp Tooth and 75g                                 (I)")
                print("Demon Bone Shiv-12 DAM, 1x Demon Bone and 100g                              (D)")
                print("Exit                                                                        (E)")
                choice=input("Choice:").upper()                                                                                  
                print_settlement()

                if choice==("R"):
                    print("You need 1x Ratling fur and 75 gold to craft Ratskin Tunic")

                    if Player.ratling_fur<1 or Player.gold<75:      
                        print("You do not have the resource to craft this item")
                        print("                                                                                            ")


                    else:
                        Player.ratling_fur-=1
                        Player.gold-=75
                        Player.inventory.append(RatskinTunic())
                        print("You gain : Ratskin Tunic")
                        print("                                                                                            ")


                elif choice==("I"):

                    print("You need 1x Imp Tooth and 75 gold to craft Imp Tooth Spear")

                    if Player.imp_tooth<1 or Player.gold<75:
                        print("You do not have the resource to craft this item")
                        print("                                                                                            ")

                    else:
                        Player.imp_tooth-=1
                        Player.gold-=75
                        Player.inventory.append(ImpToothSpear())
                        print("You gain : Imp Tooth Spear")
                        print("                                                                                            ")

                elif choice==("D"):

                    print("You need 1x Demon Bone and 100 gold to craft Demon Bone Shiv")

                    if Player.demon_bone<1 or Player.gold<100:
                        print("You do not have the resource to craft this item")
                        print("                                                                                            ")

                    else:    
                        Player.demon_bone-=1
                        Player.gold-=100
                        Player.inventory.append(DemonBoneShiv())
                        print("You gain : Demon Bone Shiv")
                        print("                                                                                            ")#
                        
                elif choice==("B"):

                    print("You need 2x Brimstone and 2x Demon Bone and 700 gold to craft Brimstone Bone Armour")

                    if Player.demon_bone<2 or Player.gold<700 or Player.brimstone<2:
                        print("You do not have the resource to craft this item")
                        print("                                                                                            ")

                    else:
                        Player.demon_bone-=2
                        Player.brimstone-=2
                        Player.gold-=700
                        Player.inventory.append(BrimstoneBoneArmour())
                        print("You gain : Brimstone Bone Armour")
                        print("                                                                                            ")
                        
                elif choice==("E"):
                    break
                        

                else:
                    print("Invalid Option")

        elif choice==("E"):
            break


        else:
            pass



def settlement_2(Player):

    while True :
        print("You stumble upon a small human settlement named 'Gloom Watch'.")
        print("Gold:",Player.gold,"Health:",Player.health,"Healing potion:",Player.healing_potion,"Mana potion:",Player.mana_potion,"Reputation:",Player.reputation)
        print("                                                                 ")

        print("Inn(I),Temple(T),Blacksmith(B) Exit(E)")
        choice=input("Choice: ").upper()
        print_settlement()
        
        if choice==("I"):
            while True:
                print("What service would you like")
                print("Rest 50g (R), Drink/Gossip 1(D), Blood Contract (B), Exit(E)" )
                choice=input("Choice:").upper()
                print_settlement()

                if choice==("R"):

                    if Player.gold<50:
                        print("You do not have enough gold to stay !!")
                        print("                                      ")

                    else:
                        Player.gold-=50
                        Player.health=Player.max_health
                        Player.mana=Player.max_mana
                        print("You wake up the next day ready for combat ")
                        print("Your health is",Player.health,"and your mana is",Player.mana)
                        print("                                      ")

                elif choice==("D"):
                    if Player.gold<1:
                        print("You do not have enough gold for an Ale ")
                        print("                                      ")

                    else:
                        Player.gold-=1
                        print("As you drink your Ale, you hear something helpful:")
                        tip=random.choice(tip_list_2)
                        print(tip)
                        print("                                      ")

                        
                elif choice==("B"):
                    if Player.sideboss_2_alive==True:            
                        Player.sidequest_2=True
                        print("Defeat the Sea Beast 'Atumbrath' at the strange caves and we will give you a map to travel though them")
                        print("The strange caves are south of here. Shout his name to summon him")
                        print("                                      ")
                    elif Player.sideboss_2_alive==False and Player.sidequest_2==True:
                        print("You have defeated the Sea Beast, here is the map. You gain 60 reputations")
                        print("I will mark the nearest settlement 'Bone Valley' outside of the caves ")
                        print("You have gain 'Caves Map'")
                        print("                                      ")
                        Player.reputation+=60
                        Player.map=True
                        Player.inventory.append("Caves Map")
                        Player.sidequest_2=False
                    else:
                        print("Thank you for slaying the Sea Beast")
                        print("                                      ")
                        
                    

                elif choice==("E"):
                    break
                    

                else:
                    print("Sorry what was that again ?")
                    print("                                      ")


        elif choice==("T"):
            while True:
                print("What service would you like ?")
                print( "Buy Potions(P),Learn Spell (S) Exit(E)")
                choice=input("Choice:").upper()
                print_settlement()

                if choice==("P"):
                    print("What type of Potions would you like?")
                    print( "Healing Potion 350g (H), Mana Potion 500g(M)")
                    choice=input("Choice:").upper()     
                    print_settlement()

                    if choice==("H"):
                        if Player.gold<350:
                            print("You do not have enough gold")
                            print("                             ")

                        else:
                            Player.healing_potion+=1
                            Player.gold-=350
                            print( "You gain a healing potion")
                            print("                             ")

                    elif choice==("M"):

                        if Player.gold<500:
                            print("You do not have enough gold")
                            print("                             ")

                        else:
                            Player.mana_potion+=1
                            Player.gold-=500
                            print( "You gain a mana potion")
                            print("                             ")
                        
                    else:
                        print_settlement()
                        print("invalid choice")
                        print("                             ")
                
                elif choice==("S"):
                    print("What spell would you like to learn")
                    print("Divine Heal 1000g(D), Ice Blast 700g(I)")
                    choice=input("Choice:").upper()     
                    print_settlement()
                    
                    if choice==("D"):

                        if Player.divine_heal==(True):
                            print("You already know the spell")
                            print("                             ")

                        elif Player.gold<1000:
                            print ("You do not have enough gold")
                            print("                             ")


                        else:
                            Player.divine_heal=True
                            Player.gold-=1000
                            print("You gain the ability to use Divine Heal")
                            print("                             ")                

                    elif choice==("I"):
                        
                        if Player.ice_blast==(True):
                            print("You already know the spell")
                            print("                             ")

                        elif Player.gold<700:

                            print ("You do not have enough gold")
                            print("                             ")
                        else:
                            Player.ice_blast=True
                            Player.gold-=700
                            print("You gain the ability to use Ice Blast")
                            print("                             ")       

                    else:
                        print("invalid option")
                        print("                             ")

                elif choice==("E"):
                    break

                else:
                    print("invalid option")
                    print("                             ")


        elif choice==("B"):
            while True: 
                print("What would you like to craft?")
                print("Demon Bone Axe-15 DAM, 2x Demon Bone and 300g                 (D)")
                print("Brimstone Mace-22 DAM,2x Brimstone, 2x Iron Shard and 500g    (B)")
                print("Silk Armour-10 PROT,2x Demon Silk and 400g                    (S)")
                print("Exit                                                          (E)")
                
                choice=input("Choice:").upper()                                                                                  
                print_settlement()

  
                if choice==("D"):

                    print("You need 2x Demon Bone and 300 gold to craft Demon Bone Axe")

                    if Player.demon_bone<2 or Player.gold<300:
                        print("You do not have enough material to craft this item")
                        print("                                                                                            ")


                    else:
                        Player.demon_bone-=2
                        Player.gold-=300
                        Player.inventory.append(DemonBoneAxe())
                        print("You gain : Demon Bone Axe")
                        print("                                                                                            ")



                elif choice==("S"):

                    print("You need 2x Demon Silk and 400 gold to craft Silk Armour")

                    if Player.demon_silk<2 or Player.gold<400:
                        print("You do not have enough material to craft this item")
                        print("                                                                                            ")


                    else:
                        Player.demon_silk-=2
                        Player.gold-=400
                        Player.inventory.append(SilkArmour())
                        print("You gain : Silk Armour")
                        print("                                                                                            ")

   
                elif choice==("B"):

                    print("You need 2x Brimstone and 2x Iron Shard and 500 gold to craft Brimstone Mace")

                    if Player.iron_shard<2 or Player.gold<500 or Player.brimstone<2 :
                        print("You do not have enough material to craft this item")
                        print("                                                                                            ")


                    else:
                        Player.iron_shard-=2
                        Player.brimstone-=2
                        Player.gold-=500
                        Player.inventory.append(BrimstoneMace())
                        print("You gain : Brimstone Mace")
                        print("                                                                                            ")



                elif choice==("E"):
                    break
                        

                else:
                    print("Invalid Option")
                    print("                                                                                            ")

        elif choice==("E"):
            break


        else:
            pass

def settlement_3(Player):

    while True :
        print("You stumble upon a small human settlement named 'Bone Valley'.")
        print("Gold:",Player.gold,"Health:",Player.health,"Healing potion:",Player.healing_potion,"Mana potion:",Player.mana_potion,"Reputation:",Player.reputation)
        print("                                                                 ")
        
        print("Inn(I),Temple(T),Blacksmith(B) Exit(E)")
        choice=input("Choice: ").upper()
        print_settlement()
        
        if choice==("I"):
            while True:
                print("What service would you like")
                print("Rest 50g (R), Drink/Gossip 1g (D), Blood Contract (B), Exit(E)" )
                choice=input("Choice:").upper()
                print_settlement()

                if choice==("R"):

                    if Player.gold<50:
                        print("You do not have enough gold to stay !!")
                        print("                                      ")
                        
                    else:
                        Player.gold-=50
                        Player.health=Player.max_health
                        Player.mana=Player.max_mana
                        print("You wake up the next day ready for combat ")
                        print("Your health is",Player.health,"and your mana is",Player.mana)    
                        print("                                      ")
                        
                elif choice==("D"):
                    if Player.gold<1:
                        print("You do not have enough gold for an Ale ")
                        print("                                      ")
                        
                    else:
                        Player.gold-=1
                        print("As you drink your Ale, you hear something helpful:")
                        tip=random.choice(tip_list_3)
                        print(tip)
                        print("                                      ")


                        
                elif choice==("B"):
                    if Player.sideboss_3_alive==True:            
                        Player.sidequest_3=True
                        print("Defeat 'Nine Dead Eyes ' the shadow stalker and you will gain a chest of crafting materials")
                        print("His hideout is south from here in a cave")
                        print("                                      ")   
                    elif Player.sideboss_3_alive==False and Player.sidequest_3==True:
                        print("You have defeated Nine Dead Eyes, here is your reward. I'll throw in 2000 gold for good measures")
                        print("5x Demon Bones, 5 x Iron Shard, 5x Brimstone, 5x Ratling Fur, 5x Demon Silk")
                        print("You gain 2000 gold and 50 reputations ")
                        print("                                      ")   
                        Player.demon_bone+=5
                        Player.iron_shard+=5
                        Player.brimstone+=5
                        Player.ratling_fur+=5
                        Player.demon_silk+=5
                        Player.gold+=2000
                        Player.reputation+=50
                        Player.sidequest_3=False
                    else:
                        print("Thank you for slaying Nine Dead Eyes")
                        print("                                      ")                      
                    

                elif choice==("E"):
                    break
                    

                else:
                    print("Sorry what was that again ?")
                    print("                                      ")   

        elif choice==("T"):
            while True:
                print("What service would you like ?")
                print( "Buy Potions(P), Knighthood (K), Learn Spell(S), Exit(E)")
                choice=input("Choice:").upper()
                print_settlement()

                if choice==("P"):
                    print("What type of Potions would you like?")
                    print( "Healing Potion 350g (H), Mana Potion 500g(M)")
                    choice=input("Choice:").upper()     
                    print_settlement()

                    if choice==("H"):
                        if Player.gold<350:
                            print("You do not have enough gold")
                            print("                             ")

                        else:
                            Player.healing_potion+=1
                            Player.gold-=350
                            print( "You gain a healing potion")
                            print("                             ")

                    elif choice==("M"):

                        if Player.gold<500:
                            print("You do not have enough gold")
                            print("                             ")

                        else:
                            Player.mana_potion+=1
                            Player.gold-=500
                            print( "You gain a mana potion")
                            print("                             ")
                        
                    else:
                        print_settlement()
                        print("invalid choice")
                        print("                             ")
                
                elif choice==("K"):

                    if Player.shadow_hunter==True or Player.doom_wizard==True:
                        print("Begone child of darkness, son of decay !! You align yourself to wickedness")
                        print("                             ")
                        
                    elif Player.holy_knight==True:
                        print("Weclome back holy child !!")
                        print("                             ")
                        
                    else:                        
                        print("You will need over 300 reputations points to upgrade your class to Holy Knight ")
                        print("                             ")
                        
                        if Player.reputation<300:
                            print ("You do not have enough reputation")
                            print("                             ")
                            
                        else:
                            choice=input("Would you like to train to be a Holy Knight? Y(Y)or(N) ").upper()

                            if choice==("Y"):
                                Player.holy_knight=True
                                Player.player_class="Holy Knight"
                                Player.max_health+=100
                                Player.health=Player.max_health
                                Player.inventory.append(HolyPlateMail())
                                Player.inventory.append(SilverSword())
                                Player.divine_heal=True
                                print("After many months of training you become a Hardened Holy Knight ")
                                print("You gain 100 max hp")
                                print("You gain Silver Sword")
                                print("You gain Holy Plate Mail")
                                print("Gain : Passive Skill 'Closer to God'( Divine Heal cost 3 less mana points )  ")
                                print("Gain : Divine Heal")
                                print("                             ")


                            else:
                                print("Come back when you are more sure")
                                print("                             ")                           
            



                elif choice==("S"):
                    print("What spell would you like to learn")
                    print("Divine Heal 1000g(D), Ice Blast 700g(I)")
                    choice=input("Choice:").upper()     
                    print_settlement()
                    
                    if choice==("D"):

                        if Player.divine_heal==(True):
                            print("You already know the spell")
                            print("                             ")

                        elif Player.gold<1000:
                            print ("You do not have enough gold")
                            print("                             ")


                        else:
                            Player.divine_heal=True
                            Player.gold-=1000
                            print("You gain the ability to use Divine Heal")
                            print("                             ")                

                    elif choice==("I"):
                        
                        if Player.ice_blast==(True):
                            print("You already know the spell")
                            print("                             ")

                        elif Player.gold<700:

                            print ("You do not have enough gold")
                            print("                             ")
                        else:
                            Player.ice_blast=True
                            Player.gold-=700
                            print("You gain the ability to use Ice Blast")
                            print("                             ")       

                    else:
                        print("invalid option")
                        print("                             ")

                elif choice==("E"):
                    break

                else:
                    print("invalid option")
                    print("                             ")



        elif choice==("B"):
            while True: 
                print("What would you like to craft?")
                print("Ratling Death Claws-32 DAM, 4x ratling furs, 2x Iron Shards, 1000g                (R)")
                print("Doom Hammer-37 DAM, 2xDemon Silk, 3x Iron Shards, 2x Demon Bones and 1500g        (D)")
                print("Heretic Plate Mail-16 PROT,3x Brimstone, 2x Iron Shard, 2x Demon Bones and 1500g  (H)")
                print("Exit                                                                              (E)")
                choice=input("Choice:").upper()                                                                                  
                print_settlement()

  
                if choice==("R"):

                    print("You need 4x ratling furs, 2x Iron Shards and 1000 gold to craft Ratling Death Claws")

                    if Player.ratling_fur<4 or Player.gold<1000 or Player.iron_shard<2:
                        print("You do not have enough material to craft this item")
                        print("                                                                                            ")


                    else:
                        Player.ratling_fur-=4
                        Player.iron_shard-=2
                        Player.gold-=1000
                        Player.inventory.append(RatlingDeathClaws())
                        print("You gain : Ratling Death Claws")
                        print("                                                                                            ")



                elif choice==("D"):

                    print("You need 2x Demon Silk, 3x Iron Shards, 2x Demon Bones and 1500 gold to craft Doom Hammer ")

                    if Player.demon_silk<2 or Player.gold<1500 or Player.iron_shard<3 or Player.demon_bone<2 :
                        print("You do not have enough material to craft this item")
                        print("                                                                                            ")


                    else:
                        Player.demon_silk-=2
                        Player.iron_shard-=3
                        Player.demon_bone-=2
                        Player.gold-=1500
                        Player.inventory.append(DoomHammer())
                        print("You gain : Doom Hammer")
                        print("                                                                                            ")

   
                elif choice==("H"):

                    print("You need 3x Brimstone, 2x Iron Shard, 2x Demon Bones and 1500 gold to craft Heretic Plate Mail")

                    if Player.iron_shard<2 or Player.gold<1500 or Player.brimstone<3 or Player.demon_bone<2  :
                        print("You do not have enough material to craft this item")
                        print("                                                                                            ")


                    else:
                        Player.iron_shard-=2
                        Player.brimstone-=3
                        Player.demon_bone-=2
                        Player.gold-=1500
                        Player.inventory.append(HereticPlateMail())
                        print("You gain : Heretic Plate Mail")
                        print("                                                                                            ")


                elif choice==("E"):
                    break
                        

                else:
                    print("Invalid Option")
                    print("                                                                                            ")

        elif choice==("E"):
            break


        else:
            pass


def settlement_4(Player):

    while True :
        print("You stumble upon a port named 'The Ship’s Biscuit'.")
        print("Gold:",Player.gold,"Health:",Player.health,"Healing potion:",Player.healing_potion,"Mana potion:",Player.mana_potion,"Reputation:",Player.reputation)
        print("                                                                 ")

        print("Inn(I),Blacksmith(B) Exit(E)")
        choice=input("Choice: ").upper()
        print_settlement()
        
        if choice==("I"):
            while True:
                print("What service would you like")
                print("Rest 50g (R), Drink/Gossip 1g (D), Blood Contract (B), Speak to the Wizard Pug (P)  Exit(E)" )
                choice=input("Choice:").upper()
                print_settlement()

                if choice==("R"):

                    if Player.gold<50:
                        print("You do not have enough gold to stay !!")
                        print("                                      ")

                    else:
                        Player.gold-=50
                        Player.health=Player.max_health
                        Player.mana=Player.max_mana
                        print("You wake up the next day ready for combat ")
                        print("Your health is",Player.health,"and your mana is",Player.mana)
                        print("                                      ")

                elif choice==("D"):
                    if Player.gold<1:
                        print("You do not have enough gold for an Ale ")
                        print("                                      ")

                    else:
                        Player.gold-=1
                        print("As you drink your Ale, you hear something helpful:")
                        tip=random.choice(tip_list_4)
                        print(tip)
                        print("                                      ")

                        
                elif choice==("B"):
                    if Player.sideboss_5_alive==True:            
                        Player.sidequest_5=True
                        print("Defeat 'Idijheh the Cultist Impaler' within the Cultist Temple of Lost Souls and we will give you a ship's deed ")
                        print("The Cultist Temple is north west from here.")
                        print("                                      ")
                    elif Player.sideboss_5_alive==False and Player.sidequest_5==True:
                        print("You have defeated Idijheh  here is your ship's deed. You gain 60 reputation")
                        print("You gain 'Ship's Deed'")
                        print("                                      ")
                        Player.inventory.append("Ship's Deed")
                        Player.reputation+=60
                        Player.ship=True
                        Player.sidequest_5=False
                    else:
                        print("Thank you for slaying Idijheh the Cultist Impaler")
                        print("                                      ")
                           
                elif choice==("P"):
                    if Player.doom_king_alive==False:
                        print("What !! You have slain the Doom King !!")
                        print("Well done but what is your next move ?")
                        print_settlement()
                        
                    else:   
                        if Player.main_quest==False:

                            print ("Pug looks at you with wild eyes and mutteres")
                            print("'My god, I think we have found the chosen one'")
                            print("                                                              ")
                            input("Press enter to continue")
                            print("                                                              ")
                            print_settlement()
                            print("'You say that you were raised from your grave and lost your memories?'")
                            print(" You nod in agreement and reply back with 'yes'      "                         )
                            print("                                                              ")
                            input("Press enter to continue")
                            print("                                                              ")
                            print_settlement()
                            print("He continues 'Do you have 3 marks on your chest that looks like a dragon ?' ")
                            print(" You shake your head since you are unaware of any strange dragon marks on your body")
                            print("                                                              ")
                            input("Press enter to continue")
                            print("                                                              ")
                            print_settlement()
                            print("'Oh sorry, you are not the chosen one, oh well maybe next time'")
                            print("                                                              ")
                            input("Press enter to continue")
                            print("                                                              ")
                            print_settlement()
                            Player.main_quest=True

                        else: 
                            print("'Are you still here ?")
                            print("Sometimes the gods play such cruel tricks on us mortals and this seems like one of them'")
                            print("                                                              ")
                            input("Press enter to continue")
                            print("                                                              ")
                            print_settlement()
                            print("'It happens once in a blue moon, we get someone who has been resurrected for apparentely no reason")
                            print("and the whole experience leaves them with memory loss, at this stage you can do what you want'")
                            print("                                                              ")
                            input("Press enter to continue")
                            print("                                                              ")
                            print_settlement()
                            print("'You can retire from adventuring and live a quiet life or ... ")
                            print("Challenge yourself to the Blood Pit of Telpo, explore the caves of Profound Misery or even.. '")
                            print("                                                              ")
                            input("Press enter to continue")
                            print("                                                              ")
                            print_settlement()
                            print("'Defeat Nizel the Doom King of the Heretic Hands and reclaim the land for the good")
                            print("The choice is yours'")
                            print("                                                              ")
                            input("Press enter to continue")
                            print("                                                              ")
                            print_settlement()

 
                    
                        
                elif choice==("E"):
                    break
                    

        elif choice==("B"):
            while True: 
                print("What would you like to craft?")
                print("Shadow Amour-25 PROT,5x Demon Silk 5x Ratling fur and 2000g               (S)")
                print("Demon Bastard Sword-45 DAM,5x Iron Shards 5x Demon Bones and 2000g        (D)")
                print("Facebreaker Gauntlet-40 DAM,8x Iron Shards and 4000g                      (F)")
                print("Exit                                                                      (E)")
                
                choice=input("Choice:").upper()                                                                                  
                print_settlement()

  
                if choice==("S"):

                    print("You need 5x Demon Silk 5x Ratling fur and 2000g to craft Shadow Amour")

                    if Player.demon_silk<5 or Player.ratling_fur<5 or Player.gold<2000:
                        print("You do not have enough material to craft this item")
                        print("                                                                                            ")


                    else:
                        Player.ratling_fur-=5
                        Player.demon_silk-=5
                        Player.gold-=2000
                        
                        Player.inventory.append(ShadowArmour())
                        print("You gain : Shadow Armour")
                        print("                                                                                            ")



                elif choice==("D"):

                    print("You need 5x Iron Shards 5x Demon Bones and 2000g to craft Demon Bastard Sword")

                    if Player.iron_shard<5 or Player.demon_bone<5 or Player.gold<2000:
                        print("You do not have enough material to craft this item")
                        print("                                                                                            ")


                    else:
                        Player.demon_bone-=5
                        Player.iron_shard-=5
                        Player.gold-=2000
                        Player.inventory.append(DemonBastardSword())
                        print("You gain : Demon Bastard Sword")
                        print("                                                                                            ")

   
                elif choice==("F"):

                    print("You need 8x Iron Shards and 3000g craft Facebreaker Gauntlet")

                    if Player.iron_shard<8 or Player.gold<3000:
                        print("You do not have enough material to craft this item")
                        print("                                                                                            ")


                    else:
                        Player.iron_shard-=8
                        Player.gold-=3000
                        Player.inventory.append(FacebreakerGauntlet())
                        print("You gain : FaceBreaker Gauntlet")
                        print("                                                                                            ")



                elif choice==("E"):
                    break
                        

                else:
                    print("Invalid Option")
                    print("                                                                                                  ")
                    
        elif choice==("E"):
            break


        else:
            pass



def settlement_5(Player):

    while True :
        print("You stumble upon a Training Settlement named 'The Red Hawk'.")
        print("Gold:",Player.gold,"Health:",Player.health,"Healing potion:",Player.healing_potion,"Mana potion:",Player.mana_potion,"Reputation:",Player.reputation)
        print("                                                                  ")
        
        print("Inn(I),Training(T),Diamond Merchant (D),  Exit(E)")
        choice=input("Choice: ").upper()
        print_settlement()
        
        if choice==("I"):
            while True:
                print("What service would you like")
                print("Rest 50g (R), Drink/Gossip 1g (D), Exit(E)" )
                choice=input("Choice:").upper()
                print_settlement()

                if choice==("R"):

                    if Player.gold<50:
                        print("You do not have enough gold to stay !!")
                        print("                                      ")
                        
                    else:
                        Player.gold-=50
                        Player.health=Player.max_health
                        Player.mana=Player.max_mana
                        print("You wake up the next day ready for combat ")
                        print("Your health is",Player.health,"and your mana is",Player.mana)    
                        print("                                      ")
                        
                elif choice==("D"):
                    if Player.gold<1:
                        print("You do not have enough gold for an Ale ")
                        print("                                      ")
                        
                    else:
                        Player.gold-=1
                        print("As you drink your Ale, you hear something helpful:")
                        tip=random.choice(tip_list_5)
                        print(tip)
                        print("                                      ")


                elif choice==("E"):
                    break
                    

                else:
                    print("Sorry what was that again ?")
                    print("                                      ")   

        elif choice==("T"):
            while True:            
                print("What Training would you like?")
                print("The Art of War (+3 Str),Cost 1 Diamond                        (W)")
                print("The Art of Magic(+3 Mana)Cost 2 Diamond                       (M)")
                print("The Art of Self-Perservation(+15 Health) Cost 1 Diamond       (S)")
                print("Exit                                                          (E)")
                choice=input("Choice:").upper()
                print_settlement()
                
                if choice==("W"):
                    if Player.diamond<1:
                        print("You do not have enough Diamond for training")
                        input("Press Enter to continue")
  
                    else:
                        Player.diamond-=1
                        Player.max_strength+=3
                        Player.strength=Player.max_strength
                        print("Your strength is now",str(Player.strength))
                        input("Press Enter to continue")


                elif choice==("M"):
                    
                    if Player.diamond<2:
                        print("You do not have enough Diamond for training")
                        input("Press Enter to continue")


                    else:
                        Player.diamond-=2
                        Player.max_mana+=3
                        Player.mana=Player.max_mana
                        print("Your mana capacity is now",str(Player.mana))
                        input("Press Enter to continue")


                elif choice==("S"):
                
                    if Player.diamond<1:
                        print("You do not have enough Diamond for training")
                        input("Press Enter to continue")


                    else:
                        Player.diamond-=1
                        Player.max_health+=15
                        Player.health=Player.max_health
                        print ("Your health is now", str(Player.health))
                        input("Press Enter to continue")
                        

                elif choice==("E"):
                    break 

                else:
                    print("Sorry one more time ? ")
                    pass
                    

            print_settlement()    
                

        elif choice==("D"):
            while True:            
                print("Would you like to trade for Diamond?")
                print("8000g for 1 Diamond              (G)  ")
                print("6x Demon Bones for 1 Diamond     (D)  ")
                print("8x Iron Shard for 1 Diamond      (I)  ")
                print("Exit                             (E)  ")
                choice=input("Choice:").upper()
                print_settlement()
                
                if choice==("G"):
                    if Player.gold<8000:
                        print("You do not have enough gold")
                        input("Press Enter to continue")

                    else:
                        Player.gold-=8000
                        Player.diamond+=1
                        print("You gain 1 Diamond")
                        input("Press Enter to continue") 

                elif choice==("D"):
                    if Player.demon_bone<6:
                        print("You do not have enough Demon Bone ")
                        input("Press Enter to continue")

                    else:
                        Player.demon_bone-=6
                        Player.diamond+=1
                        print("You gain 1 Diamond")
                        input("Press Enter to continue")

                elif choice==("I"):
                    if Player.iron_shard<8:
                        print("You do not have enough Iron Shard ")
                        input("Press Enter to continue")

                    else:
                        Player.iron_shard-=8
                        Player.diamond+=1
                        print("You gain 1 Diamond")
                        input("Press Enter to continue")
                        
                elif choice==("E"):
                    break 
                                
        elif choice==("E"):
            break
        
        else:
            pass
