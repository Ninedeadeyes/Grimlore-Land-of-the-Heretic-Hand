

# adding subclass so that in future each weapon can potentialy have
# unique function


class Weapon():    
    def __init__(self,name,damage,value):
        self.name=name
        self.damage=damage
        self.value=value
        
    def __str__(self):
        return "{}+{} DAM ".format(self.name, self.damage)

class QuarterStaff  (Weapon):
    def __init__(self,name="Wood Quarter Staff",damage=5,value=20):
        Weapon.__init__(self,name,damage,value)
        #"Wood Quarter Staff",5,20 Done


class ImpToothSpear(Weapon):
    def __init__(self,name="Imp Tooth Spear",damage=8,value=75):
        Weapon.__init__(self,name,damage,value)
        #"Imp Tooth Spear",8,75 Done
 

class DemonBoneShiv(Weapon):
     def __init__(self,name="Demon Bone Shank",damage=12,value=100):
        Weapon.__init__(self,name,damage,value)
        #"Demon Bone Shiv",12,100 Done


class DemonBoneAxe(Weapon):
    def __init__(self,name="Demon Bone Axe",damage=18,value=500):
        Weapon.__init__(self,name,damage,value)
        #"Demon Bone Axe",18,500 Done

class BrimstoneMace(Weapon):
    def __init__(self,name="Brimstone Mace",damage=22,value=700):
        Weapon.__init__(self,name,damage,value)
        #"Brimstone Mace",22,700 Done


class RatlingDeathClaws(Weapon):
    def __init__(self,name="Ratling Death Claws",damage=32,value=1200):
        Weapon.__init__(self,name,damage,value)
        #"Ratling Death Claws",32,1200  Done


class DoomHammer(Weapon):
    def __init__(self,name="Doom Hammer",damage=37,value=1500):
        Weapon.__init__(self,name,damage,value)
        #"Doom Hammer",37,1500  Done


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
        return "{}+{} PROT ".format(self.name, self.protection)


class Rags(Armour):
    def __init__(self,name="Rags",protection=0,value=20):
        Armour.__init__(self,name,protection,value)
       #rags,0,20  Done


class RatskinTunic(Armour):
    def __init__(self,name="Ratskin Tunic",protection=3,value=75):
        Armour.__init__(self,name,protection,value)
      #Ratskin Tunic,3,75 Done

class SilkArmour(Armour):
    def __init__(self,name="Silk Armour",protection=7,value=100):
        Armour.__init__(self,name,protection,value)
      #"Silk Armour",7,100  Done



class BrimstoneBoneArmour (Armour):
    def __init__(self,name="Brimstone Bone Armour",protection=12,value=100):
        Armour.__init__(self,name,protection,value)
        #"Brimstone Bone Armour",12,100 Done


class HereticPlateMail (Armour):
    def __init__(self,name="Heretic Plate Mail",protection=16,value=100):
        Armour.__init__(self,name,protection,value)
        #"Heretic Plate Mail",16,100 Done


class ShadowArmour (Armour):
    def __init__(self,name="Shadow Armour",protection=25,value=100):
        Armour.__init__(self,name,protection,value)
       #"Shadow Armour",25,100  Done


class HolyPlateMail (Armour):
    def __init__(self,name="Holy Plate Mail",protection=35,value=100):
        Armour.__init__(self,name,protection,value)
        #"Holy Plate Mail",35,100 Done


class DoomKingPlateMail (Armour):
    def __init__(self,name="Doom King Plate Mail",protection=50,value=100):
        Armour.__init__(self,name,protection,value)
        #"Doom King Plate Mail",50,100 Done
