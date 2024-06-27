

# adding subclass so that in future each weapon can potentialy have
# unique function


class Weapon():    
    def __init__(self,name,damage,value):
        self.name=name
        self.damage=damage
        self.value=value
        
    def __str__(self):
        return "{}+{} DAM ".format(self.name, self.damage)   # Not used in game yet but will be useful if I ever weapon index for the game 

class QuarterStaff  (Weapon):
    def __init__(self,name="Wood Quarter Staff",damage=5,value=20):
        Weapon.__init__(self,name,damage,value)
        #"Wood Quarter Staff",5,20 Done


class ImpToothSpear(Weapon):
    def __init__(self,name="Imp Tooth Spear",damage=10,value=75):
        Weapon.__init__(self,name,damage,value)
        #"Imp Tooth Spear",10,75 Done
 

class DemonBoneShiv(Weapon):
     def __init__(self,name="Demon Bone Shank",damage=14,value=100):
        Weapon.__init__(self,name,damage,value)
        #"Demon Bone Shiv",14,100 Done


class DemonBoneAxe(Weapon):
    def __init__(self,name="Demon Bone Axe",damage=20,value=500):
        Weapon.__init__(self,name,damage,value)
        #"Demon Bone Axe",20,500 Done

class BrimstoneMace(Weapon):
    def __init__(self,name="Brimstone Mace",damage=24,value=700):
        Weapon.__init__(self,name,damage,value)
        #"Brimstone Mace",24,700 Done


class RatlingDeathClaws(Weapon):
    def __init__(self,name="Ratling Death Claws",damage=34,value=1200):
        Weapon.__init__(self,name,damage,value)
        #"Ratling Death Claws",34,1200  Done


class DoomHammer(Weapon):
    def __init__(self,name="Doom Hammer",damage=39,value=1500):
        Weapon.__init__(self,name,damage,value)
        #"Doom Hammer",39,1500  Done


class SilverSword(Weapon):
    def __init__(self,name="Silver Sword",damage=50,value=1500):
        Weapon.__init__(self,name,damage,value)
        #"Silver Sword",50,1500 Done


class ShadowBlade(Weapon):
    def __init__(self,name="Shadow Blade",damage=75,value=1500):
        Weapon.__init__(self,name,damage,value)
        #"Shadow Blade ",75,1500  Done

class DemonBastardSword(Weapon):
    def __init__(self,name="Demon Bastard Sword",damage=45,value=1500):
        Weapon.__init__(self,name,damage,value)
        #"Demon Bastard Sword",45,1500  Done

class FacebreakerGauntlet(Weapon):
    def __init__(self,name="FaceBreaker Gauntlet",damage=40,value=1500):
        Weapon.__init__(self,name,damage,value)
        #"FaceBreaker Gauntlet",40,1500  Done

class DoomKingSword(Weapon):
    def __init__(self,name="Doom King Sword",damage=75,value=1500):
        Weapon.__init__(self,name,damage,value)
        #Doom King Sword ",75,1500 Done


class Armour():  
    def __init__(self,name,protection,value):
        self.name=name
        self.protection=protection
        self.value= value
        
    def __str__(self):
        return "{}+{} PROT ".format(self.name, self.protection)   # Not used in game yet but will be useful if I ever armour index for the game 

class Rags(Armour):
    def __init__(self,name="Rags",protection=1,value=20):
        Armour.__init__(self,name,protection,value)
       #rags,1,20  Done


class RatskinTunic(Armour):
    def __init__(self,name="Ratskin Tunic",protection=5,value=75):
        Armour.__init__(self,name,protection,value)
      #Ratskin Tunic,5,75 Done

class SilkArmour(Armour):
    def __init__(self,name="Silk Armour",protection=12,value=100):
        Armour.__init__(self,name,protection,value)
      #"Silk Armour",10,100  Done



class BrimstoneBoneArmour (Armour):
    def __init__(self,name="Brimstone Bone Armour",protection=15,value=100):
        Armour.__init__(self,name,protection,value)
        #"Brimstone Bone Armour",15,100 Done


class HereticPlateMail (Armour):
    def __init__(self,name="Heretic Plate Mail",protection=24,value=100):
        Armour.__init__(self,name,protection,value)
        #"Heretic Plate Mail",24,100 Done


class ShadowArmour (Armour):
    def __init__(self,name="Shadow Armour",protection=30,value=100):
        Armour.__init__(self,name,protection,value)
       #"Shadow Armour",30,100  Done


class HolyPlateMail (Armour):
    def __init__(self,name="Holy Plate Mail",protection=35,value=100):
        Armour.__init__(self,name,protection,value)
        #"Holy Plate Mail",35,100 Done


class DoomKingPlateMail (Armour):
    def __init__(self,name="Doom King Plate Mail",protection=55,value=100):
        Armour.__init__(self,name,protection,value)
        #"Doom King Plate Mail",40,100 Done
