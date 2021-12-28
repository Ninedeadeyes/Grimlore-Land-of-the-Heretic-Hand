

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
    def __init__(self,name,damage,value):
        Weapon.__init__(self,name,damage,value)
        #"Wood Quarter Staff ",5,20


class ImpToothSpear(Weapon):
    def __init__(self,name,damage,value):
        Weapon.__init__(self,name,damage,value)
        #"Imp Tooth Spear",8,75
 

class DemonBoneShiv(Weapon):
     def __init__(self,name,damage,value):
        Weapon.__init__(self,name,damage,value)
        #"Demon Bone Shiv",12,100


class DemonBoneAxe(Weapon):
    def __init__(self,name,damage,value):
        Weapon.__init__(self,name,damage,value)
        #"Demon Bone Axe",18,500

class BrimstoneMace(Weapon):
    def __init__(self,name,damage,value):
        Weapon.__init__(self,name,damage,value)
        #"Brimstone Mace",22,700


class RatlingDeathClaws(Weapon):
    def __init__(self,name,damage,value):
        Weapon.__init__(self,name,damage,value)
        #"Ratling Death Claws",32,1200


class DoomHammer(Weapon):
    def __init__(self,name,damage,value):
        Weapon.__init__(self,name,damage,value)
        #"Doom Hammer",37,1500


class SilverSword(Weapon):
    def __init__(self,name,damage,value):
        Weapon.__init__(self,name,damage,value)
        #"Silver Sword",50,1500


class ShadowBlade(Weapon):
    def __init__(self,name,damage,value):
        Weapon.__init__(self,name,damage,value)
        #"Shadow Blade ",75,1500

class DemonBastardSword(Weapon):
    def __init__(self,name,damage,value):
        Weapon.__init__(self,name,damage,value)
        #"Demon Bastard Sword",45,1500

class FacebreakerGauntlet(Weapon):
    def __init__(self,name,damage,value):
        Weapon.__init__(self,name,damage,value)
        #"FaceBreaker Gauntlet",40,1500

class DoomKingSword(Weapon):
    def __init__(self,name,damage,value):
        Weapon.__init__(self,name,damage,value)
        #Doom King Sword ",75,1500


class Armour():  
    def __init__(self,name,protection,value):
        self.name=name
        self.protection=protection
        self.value= value
        
    def __str__(self):
        return "{}+{} PROT ".format(self.name, self.protection)


class Rags(Armour):
    def __init__(self,name,protection,value):
        Armour.__init__(self,name,protection,value)
       #rags,0,20


class RatskinTunic(Armour):
    def __init__(self,name,protection,value):
        Armour.__init__(self,name,protection,value)
      #Ratskin Tunic,3,75

class SilkArmour(Armour):
    def __init__(self,name,protection,value):
        Armour.__init__(self,name,protection,value)
      #"Silk Armour",7,100



class BrimstoneBoneArmour (Armour):
    def __init__(self,name,protection,value):
        Armour.__init__(self,name,protection,value)
        #"Brimstone Bone Armour",12,100


class HereticPlateMail (Armour):
    def __init__(self,name,protection,value):
        Armour.__init__(self,name,protection,value)
        #"Heretic Plate Mail",16,100


class ShadowArmour (Armour):
    def __init__(self,name,protection,value):
        Armour.__init__(self,name,protection,value)
       #"Shadow Armour",25,100


class HolyPlateMail (Armour):
    def __init__(self,name,protection,value):
        Armour.__init__(self,name,protection,value)
        #"Holy Plate Mail",35,100


class DoomKingPlateMail (Armour):
    def __init__(self,name,protection,value):
        Armour.__init__(self,name,protection,value)
        #"Doom King Plate Mail",50,100
