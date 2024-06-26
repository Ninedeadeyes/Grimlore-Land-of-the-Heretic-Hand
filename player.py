import sys
import random
from items import*
from enemy import*
import winsound
import time
from animation import ending

class Player(object):
    def __init__ (self,health,gold,strength,mana,exp,healing_potion,mana_potion):
        self.inventory=["Spell book"]
        self.armour=Rags()
        self.weapon=QuarterStaff()
        self.talisman="None"
        self.level=1
        self.gold=0
        self.health=100
        self.max_health=100
        self.strength=12
        self.max_strength=12
        self.max_mana=5
        self.mana=5
        self.exp=0
        self.healing_potion=healing_potion
        self.mana_potion=mana_potion
        self.imp_tooth=0
        self.ratling_fur=0
        self.demon_bone=0
        self.demon_silk=0
        self.iron_shard=0
        self.brimstone=0
        self.diamond=0
        self.fire_bolt=False
        self.divine_heal=False
        self.shadow_flee=False
        self.ice_blast=False
        self.chaos_vortex=False
        self.flee=False
        self.dungeon=False
        self.sidequest_1=False
        self.sideboss_1_alive=True
        self.sidequest_2=False
        self.sideboss_2_alive=True
        self.sidequest_3=False
        self.sideboss_3_alive=True
        self.sidequest_3_escape=False
        self.sideboss_4_alive=True
        self.sidequest_5=False
        self.sideboss_5_alive=True
        self.main_quest=False
        self.doom_king_alive=True
        self.turn_counter=0
        self.marks=False
        self.map=False
        self.ship=False
        self.amulet=False
        self.player_class="Struggler"
        self.reputation=0
        self.shadow_hunter=False
        self.holy_knight=False
        self.doom_wizard=False
        self.diamond_1=False
        self.diamond_2=False
        self.diamond_3=False
        self.diamond_4=False
        self.diamond_5=False
        self.abandoned_outpost=False
        self.level2_claimed = False
        self.level3_claimed = False
        self.level4_claimed = False
        self.level5_claimed = False
        self.level6_claimed = False
        self.level7_claimed = False
        self.level8_claimed = False
        self.level9_claimed = False
        self.level10_claimed = False
        self.level11_claimed = False
        self.level12_claimed = False
        self.level13_claimed = False
        self.level14_claimed = False
        self.level15_claimed = False
        self.level16_claimed = False
        self.level17_claimed = False
        self.level18_claimed = False
        self.level19_claimed = False
        self.level20_claimed = False


    def level_up(self):
        while True:
            print ( "What would you like to increase ? Health (H), Strength (S), Mana(M)")
            upgrade=input("Choice:").upper()
            print("\033c")

            if upgrade == "H":
                self.max_health+=20
                self.mana=self.max_mana
                self.health=self.max_health
                print ("Your health is now", str(self.health))
                break
               
                
            elif upgrade == "S":
                self.max_strength+=5
                self.strength=self.max_strength
                self.mana=self.max_mana
                self.health=self.max_health
                print("Your strength is now", str(self.strength))
                break

            elif upgrade=="M":
                self.max_mana+=3
                self.mana=self.max_mana
                self.health=self.max_health
                print("Your mana capacity is now",str(self.mana))
                break


            else:
                print("invalid choice")
                
    def fight (self,Enemy):
            
       
        print(Enemy.name+" hp:"+str(Enemy.hp)+ " Str:" +str(Enemy.strength))
        
        while True:
            self.flee=False
            print("                                                                                                                                                   ")
            print("Health",self.health,"STR",(self.strength+self.weapon.damage),"Mana:",self.mana,"Healing potion:",self.healing_potion,"Mana potion:",self.mana_potion)
            print("What is your next action: Attack (A), Escape(E), Use (U), Magic(M) ")
            choice=input("Choice: ")
            choice=choice.upper()
            print("\033c")
            
            if choice==("A"):

                enemy_special_dice=random.randint(1,10)
                if enemy_special_dice==10:


                    if Enemy.special==("bloodlust") :              # Lesser Demon,Hell Hound, Iron Tusk Demon, Greater Demon, butcher, demon troll, 
                        Enemy.strength+=2
                        print("The stench of blood fills the",Enemy.name,"with a killer instinct")
                        print(Enemy.name,"gain a permanent +2 to strength")
                        print("The battle continues.. ")

                    if Enemy.special==("heal1") :               #Sea Beast, Clockwork Pain Taker
                        if Enemy.hp<300:
                            heal_dice=random.randint(50,125)
                            Enemy.hp+=heal_dice
                            print("The",Enemy.name,"starts to regenerate his wounds")
                            print("The",Enemy.name,"gain", str(heal_dice),"hp. The",Enemy.name,"hp is now",Enemy.hp )
                            print("The battle continues.. ")
                    
                    if Enemy.special==("heal2") :               # Doom King
                        if Enemy.hp<1500:
                            heal_dice=random.randint(100,500)
                            Enemy.hp+=heal_dice
                            print(Enemy.name,"starts to regenerate his wounds")
                            print(Enemy.name,"gain", str(heal_dice),"hp. The",Enemy.name,"hp is now",Enemy.hp )
                            print("The battle continues.. ")
                    
                    
                    if Enemy.special==("drain") :                   #Fallen Knight, Ratling Mage
                        if self.mana>0:
                            self.mana=0
                            print("The",Enemy.name,"drains you dry of mana")
                            print("Your mana has dropped to 0. Time to hack and slash!" )
                            print("The battle continues.. ")    

                event=random.randint(1,10)

                if event==1:
                    dice2=random.randint(1,12)
                    player_damage=self.strength+dice2+self.weapon.damage
                    Enemy.hp-=player_damage
                    print("The",Enemy.name,"attacks you but you dodge the strike. ")
                    print("As the",Enemy.name,"regains his composure...")
                    print("You attack the",Enemy.name,"and deal",player_damage,"damage. The",Enemy.name,"health is "+ str(Enemy.hp))

                elif event==2:
                    dice1=random.randint(1,12)
                    dice2=random.randint(1,12)
                    dice_prot=random.randint(0,2)
                    point_prot=dice_prot+self.armour.protection
                    crit=round((Enemy.strength+dice1)*1.25)
                    enemy_damage=max(0,crit-point_prot)
                    self.health-=enemy_damage
                    player_damage=self.strength+dice2+self.weapon.damage
                    Enemy.hp-=player_damage
                    print("The",Enemy.name,"lands a critical hit of",enemy_damage,"damage. Your health is",str(self.health))
                    print("Your armour protected you for",point_prot,"damage")
                    print("You attack the",Enemy.name,"and deal",player_damage,"damage. The",Enemy.name,"health is "+ str(Enemy.hp))

    
                else:
                    dice1=random.randint(1,12)
                    dice2=random.randint(1,12)
                    dice_prot=random.randint(0,2)
                    point_prot=dice_prot+self.armour.protection
                    enemy_damage=max(0,Enemy.strength+dice1-point_prot)
                    self.health-=enemy_damage
                    player_damage=self.strength+dice2+self.weapon.damage
                    Enemy.hp-=player_damage
                    print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                    print("Your armour protected you for",point_prot,"damage")
                    print("You attack the",Enemy.name,"and deal",player_damage,"damage. The",Enemy.name,"health is "+ str(Enemy.hp))
                
                if self.shadow_hunter==True:

                    r=random.random()
                    if r <.50:
                        dice3=random.randint(1,20)
                        Enemy.hp-=dice3
                        print("You deliver an additional body blow, you deal",dice3,"additional damage")
                                
                    elif r <.75:
                        
                        dice3=random.randint(10,20)
                        Enemy.hp-=(self.strength+dice3+self.weapon.damage)
                        damage=(self.strength+dice3+self.weapon.damage)
                        print("You execute a critical hit you deal",damage,"additional damage")

                    elif r <.75:
                        dice3=random.randint(30,150)
                        Enemy.hp-=dice3
                        print("You use the infamous 'Shadow Death Grip' technique you deal",dice3,"additional damage" )

                    else:
                        print("You are not able to execute any of your Shadow Hunter's techniques this round")
                        
                        
            elif choice==("M"):
                while True:
                    print ("What spell would you like to cast ?" )
                    if self.fire_bolt==True:
                        print("Fire Bolt 4 mana        (F)")
                    if self.shadow_flee==True:
                        print("Shadow Flee 2 mana      (S)")
                    if self.ice_blast==True:
                        print("Ice Blast 5 mana        (I)")
                    if self.divine_heal==True:
                        print("Divine Heal 7/4 mana    (D)")
                    if self.chaos_vortex==True:
                        print("Chaos Vortex 6 mana     (V)")
                    print("Exit                    (E)")
                    spell=input("Spell: ")
                    spell=spell.upper()

                    if spell==("F"):
                        if self.fire_bolt==True and self.mana>=4:
                            power=random.randint(70,120)
                            Enemy.hp-=power
                            self.mana-=4
                            print("You cast a fire bolt at the "+Enemy.name+". You deal",power,"fire damage. The "+Enemy.name+" health is "+ str(Enemy.hp))
                            print("The "+Enemy.name+" is set alight and is unable to attack back")

                            break

                        else:
                            print("You do not have the ablity or the mana to cast the spell")
                            dice1=random.randint(1,12)
                            dice_prot=random.randint(0,2)
                            point_prot=dice_prot+self.armour.protection
                            enemy_damage=max(0,Enemy.strength+dice1-point_prot)
                            self.health-=enemy_damage
                            print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                            print("Your armour protected you for",point_prot,"damage")
                            break

                    elif spell==("D"):
                        if self.holy_knight==True:

                            if self.divine_heal==True and self.mana>=4:
                                self.mana-=4
                                self.health=self.max_health
                                print("You feel the light of God shine through the bleakest darkness")
                                print("Mana cost for divine heal is reduce to 4 ")
                                print("You have fully recovered your health")
                                dice1=random.randint(1,12)
                                enemy_damage=max(0,Enemy.strength+dice1-self.armour.protection)
                                self.health-=enemy_damage
                                print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                                print("Your armour protected you for",self.armour.protection,"damage")
                                break

                            else:
                                print("You do not have the ablity or the mana to cast the spell")
                                dice1=random.randint(1,12)
                                dice_prot=random.randint(0,2)
                                point_prot=dice_prot+self.armour.protection
                                enemy_damage=max(0,Enemy.strength+dice1-point_prot)
                                self.health-=enemy_damage
                                print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                                print("Your armour protected you for",point_prot,"damage")
                                break

                        else:
                            
                            if self.divine_heal==True and self.mana>=7:
                                self.mana-=7
                                self.health=self.max_health
                                print("You have fully recover your health")
                                dice1=random.randint(1,12)
                                enemy_damage=max(0,Enemy.strength+dice1-self.armour.protection)
                                self.health-=enemy_damage
                                print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                                print("Your armour protected you for",self.armour.protection,"damage")
                                break

                            else:
                                print("You do not have the ablity or the mana to cast the spell")
                                dice1=random.randint(1,12)
                                dice_prot=random.randint(0,2)
                                point_prot=dice_prot+self.armour.protection
                                enemy_damage=max(0,Enemy.strength+dice1-point_prot)
                                self.health-=enemy_damage
                                print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                                print("Your armour protected you for",point_prot,"damage")
                                break
                        

                    elif spell==("S"):

                        if self.dungeon==True:
                            print("You cannot escape in a dungeon")
                            dice1=random.randint(1,12)
                            enemy_damage=max(0,Enemy.strength+dice1-self.armour.protection)
                            self.health-=enemy_damage
                            print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                            print("Your armour protected you for",self.armour.protection,"damage")
                            break
                        
                        elif self.shadow_flee==True and self.mana>=2:
                            self.mana-=2
                            self.flee=True
                            break

                        else:
                            print("You do not have the ablity or the mana to cast the spell")
                            dice1=random.randint(1,12)
                            dice_prot=random.randint(0,2)
                            point_prot=dice_prot+self.armour.protection
                            enemy_damage=max(0,Enemy.strength+dice1-point_prot)
                            self.health-=enemy_damage
                            print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                            print("Your armour protected you for",point_prot,"damage")
                            break


                    elif spell==("I"):
                        if self.ice_blast==True and self.mana>=5:
                            power=random.randint(60,100)
                            Enemy.hp-=power
                            self.mana-=5

                            if self.shadow_hunter==True:
                                print("You deal",power,"Ice damage.The "+Enemy.name+" is frozen stiff,.You are able to get an extra 3 hits with your mastery of shadow combat ")
                                dice2=random.randint(1,12)
                                player_damage=self.strength+dice2+self.weapon.damage
                                Enemy.hp-=(player_damage)
                                print("You attack the",Enemy.name,"and deal",player_damage,"damage. The",Enemy.name,"health is "+ str(Enemy.hp))
                                dice2=random.randint(1,12)
                                player_damage=self.strength+dice2+self.weapon.damage
                                Enemy.hp-=(player_damage)
                                print("You attack the",Enemy.name,"and deal",player_damage,"damage. The",Enemy.name,"health is "+ str(Enemy.hp))
                                dice2=random.randint(1,12)
                                player_damage=self.strength+dice2+self.weapon.damage
                                Enemy.hp-=(player_damage)
                                print("You attack the",Enemy.name,"and deal",player_damage,"damage. The",Enemy.name,"health is "+ str(Enemy.hp))
                                break

                            else:

                                print("You deal",power,"Ice damage.The "+Enemy.name+" is frozen stiff,.You are able to get an extra 2 hits")
                                dice2=random.randint(1,12)
                                player_damage=self.strength+dice2+self.weapon.damage
                                Enemy.hp-=(player_damage)
                                print("You attack the",Enemy.name,"and deal",player_damage,"damage. The",Enemy.name,"health is "+ str(Enemy.hp))
                                dice2=random.randint(1,12)
                                player_damage=self.strength+dice2+self.weapon.damage
                                Enemy.hp-=(player_damage)
                                print("You attack the",Enemy.name,"and deal",player_damage,"damage. The",Enemy.name,"health is "+ str(Enemy.hp))
                                break

                        else:
                            print("You do not have the ablity or the mana to cast the spell")
                            dice1=random.randint(1,12)
                            dice_prot=random.randint(0,2)
                            point_prot=dice_prot+self.armour.protection
                            enemy_damage=max(0,Enemy.strength+dice1-point_prot)
                            self.health-=enemy_damage
                            print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                            print("Your armour protected you for",point_prot,"damage")
                            break

                    elif spell==("V"):
                        if self.chaos_vortex==True and self.mana>=6:
                            power=random.randint(200,500)
                            Enemy.hp-=power
                            self_damage=random.randint(5,40)
                            self.health-=self_damage
                            self.mana-=6
                            print("You deal",power,"Chaos damage.The "+Enemy.name+" is stun for the round. The",Enemy.name,"health is "+ str(Enemy.hp))
                            print("But such power does not come without sacrifice, Chaos vortex inflicts",self_damage,"to you. Your health is",str(self.health))
                            break
                            

                        else:
                            print("You do not have the ablity or the mana to cast the spell")
                            dice1=random.randint(1,12)
                            dice_prot=random.randint(0,2)
                            point_prot=dice_prot+self.armour.protection
                            enemy_damage=max(0,Enemy.strength+dice1-point_prot)
                            self.health-=enemy_damage
                            print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                            print("Your armour protected you for",point_prot,"damage")
                            break

                    elif spell==("E"):
                            print("You decide not to cast a spell. What is your next action ?")
                            break
                            
                
                    else:
                        print("invalid option")         

            elif choice==("E"):
                if self.dungeon==True:
                    print("You cannot escape in a dungeon")
                    dice1=random.randint(1,12)
                    dice_prot=random.randint(0,2)
                    point_prot=dice_prot+self.armour.protection
                    enemy_damage=max(0,Enemy.strength+dice1-point_prot)
                    self.health-=enemy_damage
                    print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                    print("Your armour protected you for",point_prot,"damage")
                else:
                    
                     r= random.random()
                     if r < .40:
                         print("You manage to escape")
                         input("press enter to continue")
                         self.flee=True
                         break
                     else:
                         print ("You do not escape")
                         dice1=random.randint(1,12)
                         dice_prot=random.randint(0,2)
                         point_prot=dice_prot+self.armour.protection
                         enemy_damage=max(0,Enemy.strength+dice1-point_prot)
                         self.health-=enemy_damage
                         print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                         print("Your armour protected you for",point_prot,"damage")

            elif choice==("U"):
                while True:
                    print ("What would you like to use ? Healing Potion +250 Enemy.hp(H), Mana Potion +25 Mana(M), Exit(E)")
                    choice=input("Use:")
                    choice=choice.upper()
                    
                    if choice==("H"):
                    
                        if self.healing_potion>0:
                            self.healing_potion-=1
                            heal=250
                            self.health=min(self.max_health,self.health+heal)
                            print( "you drink a healing potion")
                            print("Your health is", str(self.health))
                            dice1=random.randint(1,12)
                            enemy_damage=max(0,Enemy.strength+dice1-self.armour.protection)
                            self.health-=enemy_damage
                            print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                            print("Your armour protected you for",self.armour.protection,"damage")
                            break
                        
                        else:
                            print("you have no more healing potion")
                            dice1=random.randint(1,12)
                            dice_prot=random.randint(0,2)
                            point_prot=dice_prot+self.armour.protection
                            enemy_damage=max(0,Enemy.strength+dice1-point_prot)
                            self.health-=enemy_damage
                            print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                            print("Your armour protected you for",point_prot,"damage")
                            break


                    elif choice==("M"):
                    
                        if self.mana_potion>0:
                            self.mana_potion-=1
                            recharge=25
                            self.mana=min(self.max_mana,self.mana+recharge)
                            print( "you drink a mana potion")
                            print("Your mana is", str(self.mana))
                            dice1=random.randint(1,12)
                            dice_prot=random.randint(0,2)
                            point_prot=dice_prot+self.armour.protection
                            enemy_damage=max(0,Enemy.strength+dice1-point_prot)
                            self.health-=enemy_damage
                            print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                            print("Your armour protected you for",point_prot,"damage")
                            break
                        else:
                            print("you have no more mana potion")
                            dice1=random.randint(1,12)
                            dice_prot=random.randint(0,2)
                            point_prot=dice_prot+self.armour.protection
                            enemy_damage=max(0,Enemy.strength+dice1-point_prot)
                            self.health-=enemy_damage
                            print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                            print("Your armour protected you for",point_prot,"damage")
                            break

                    elif spell==("E"):
                            print("You decide not to use an item. What is your next action ?")
                            break


                            
                    else:
                        print("invalid option")
                        dice1=random.randint(1,12)
                        dice_prot=random.randint(0,2)
                        point_prot=dice_prot+self.armour.protection
                        enemy_damage=max(0,Enemy.strength+dice1-point_prot)
                        self.health-=enemy_damage
                        print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                        print("Your armour protected you for",point_prot,"damage")
                        break

            else:
                print ("invalid option")
                dice1=random.randint(1,12)
                dice_prot=random.randint(0,2)
                point_prot=dice_prot+self.armour.protection
                enemy_damage=max(0,Enemy.strength+dice1-point_prot)
                self.health-=enemy_damage
                print("The",Enemy.name,"attacks you for",enemy_damage,"damage. Your health is",str(self.health))
                print("Your armour protected you for",point_prot,"damage")
                            

            if self.flee==True:
                input("You disappear into the shadows, to fight another day ")
                break
            
            
            elif self.health<=0:
                if self.talisman==("Resurrection"):
                    self.health=self.max_health
                    self.talisman=("None")
                    print("You have been slained. Your Resurrection Talisman is activated ")
                    print("[You lose : 1x Resurrection Talisman]")
                    self.inventory.remove("Resurrection Talisman")
                    input("Press any key to continue your struggle")
                



                else :   
                    time.sleep(1)
                    #print("\033c")
                    winsound.PlaySound(".\\music\\rip.wav",winsound.SND_ALIAS | winsound.SND_ASYNC) 
                    ending()  #animation 
                    print("Wounds upon wounds, you fall in battle")
                    print("You have lost against the consuming darkness ")
                    print("""   
                                            MM                                                        
                                            MM                                                        
                                            MM                                                        
                                            MM                                                        
                                            MM                                                        
                                            MM                                                        
                        yyyyyyyyyyyyyyyyyyyyMMyyyyyyyyyyyyyyyyyyyy                                    
                        ++++++++++++++++++++MM++++++++++++++++++++                                    
                                            MM                                                        
                                            MM                                                        
                                            MM                                                        
                                            MM                                                        
                                            MM                                                        
                                            MM                                                        
                                            MM                                                        
                                            MM                                                        
                                            MM                                                        
                                            MM                                                        
                                            MM                                                        
                                            MM        ////////                                        
                                            MM      //yyyyyyyy//                                      
                                            MM      MM        MM                                      
                                            MM      MM        MM                                      
                                            MM      MM  MMMM  MM                                      
                                            MM      MM  MMMM  MM                                      
                                            MM      MM  MMMM  MM                                      
                        --dddddddddddddddddddddddddddddddddddddd--                                    
                        --dd                                      dd--                                  
    ------------------dd                                          dd------------------                
    mmmmmmmmmmmmmmmmmm                                              mmmmmmmmmmmmmmmmmm                
                                                                                                                                                                
                                                                            
                                                                                

    """) 

                    time.sleep(2)
                    input("Press enter to quit")  
                    sys.exit()

            elif Enemy.hp<=0:
                print("You have slain the "+Enemy.name)
                print ("you gain", str(Enemy.gold),"gold" )
                print("you gain",str(Enemy.xp),"exp")
                self.gold+=Enemy.gold
                self.exp+=Enemy.xp
                r= random.random()
                if r <.50:
                    if Enemy.item ==("Imp Tooth"):
                        self.imp_tooth+=1
                        print("You gain : Imp Tooth")
                    elif Enemy.item==("Ratling Fur"):
                        self.ratling_fur+=1
                        print("You gain : Ratlng Fur")
                    elif Enemy.item==("Demon Bone"):
                        self.demon_bone+=1
                        print("You gain : Demon Bone")
                    elif Enemy.item ==("Brimstone"):
                        self.brimstone+=1
                        print("You gain : Brimstone")
                    elif Enemy.item==("Iron Shard"):
                        self.iron_shard+=1
                        print("You gain : Iron Shard")
                    elif Enemy.item==("Demon Silk"):
                        self.demon_silk+=1
                        print("You gain : Demon Silk")

                else:
                    print("There is nothing of value left on the corpse")
                    pass
                    
                
                if self.exp>100 and self.level2_claimed ==False:
                    print("You are now level 2")
                    self.level_up()
                    self.level2_claimed = True
                    self.level=2

                elif self.exp>250 and self.level3_claimed ==False:
                    print("You are now level 3")
                    self.level_up()
                    self.level3_claimed = True
                    self.level=3

                elif self.exp>500 and self.level4_claimed ==False:
                    print("You are now level 4")
                    self.level_up()
                    self.level4_claimed = True
                    self.level=4

                elif self.exp>1000 and self.level5_claimed ==False:
                    print("You are now level 5")
                    self.level_up()
                    self.level5_claimed = True
                    self.level=5


                elif self.exp>1800 and self.level6_claimed ==False:
                    print("You are now level 6")
                    self.level_up()
                    self.level6_claimed = True
                    self.level=6

                elif self.exp>3000 and self.level7_claimed ==False:
                    print("You are now level 7")
                    self.level_up()
                    self.level7_claimed = True
                    self.level=7

                elif self.exp>5000 and self.level8_claimed ==False:
                    print("You are now level 8")
                    self.level_up()
                    self.level8_claimed = True
                    self.level=8

                elif self.exp>8000 and self.level9_claimed ==False:
                    print("You are now level 9")
                    self.level_up()
                    self.level9_claimed = True
                    self.level=9

                elif self.exp>12000 and self.level10_claimed ==False:
                    print("You are now level 10")
                    self.level_up()
                    self.level10_claimed = True
                    self.level=10

                if self.exp>17000 and self.level11_claimed ==False:
                    print("You are now level 11")
                    self.level_up()
                    self.level11_claimed = True
                    self.level=11

                if self.exp>24000 and self.level12_claimed ==False:
                    print("You are now level 12")
                    self.level_up()
                    self.level12_claimed = True
                    self.level=12

                elif self.exp>32000 and self.level13_claimed ==False:
                    print("You are now level 13")
                    self.level_up()
                    self.level13_claimed = True
                    self.level=13

                elif self.exp>42000 and self.level14_claimed ==False:
                    print("You are now level 14")
                    self.level_up()
                    self.level14_claimed = True
                    self.level=14

                elif self.exp>54000 and self.level15_claimed ==False:
                    print("You are now level 15")
                    self.level_up()
                    self.level15_claimed = True
                    self.level=15


                elif self.exp>68000 and self.level16_claimed ==False:
                    print("You are now level 16")
                    self.level_up()
                    self.level16_claimed = True
                    self.level=16

                elif self.exp>82000 and self.level17_claimed ==False:
                    print("You are now level 17")
                    self.level_up()
                    self.level17_claimed = True
                    self.level=17

                elif self.exp>100000 and self.level18_claimed ==False:
                    print("You are now level 18")
                    self.level_up()
                    self.level18_claimed = True
                    self.level=18

                elif self.exp>150000 and self.level19_claimed ==False:
                    print("You are now level 19")
                    self.level_up()
                    self.level19_claimed = True
                    self.level=19

                elif self.exp>200000 and self.level20_claimed ==False:
                    print("You are now level 20")
                    self.level_up()
                    self.level20_claimed = True
                    self.level=20

                input("Press enter to continue to adventure")
                break
            
