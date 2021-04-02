
class Weapon():  
    def __init__(self):
        raise NotImplementedError("Do not create raw Armour Objects.")

    def __str__(self):
        return "{}+{} DAM ".format(self.name, self.damage)

class QuarterStaff  (Weapon):
    def __init__(self,name,damage,value):
        self.name="Wood Quarter Staff "
        self.damage=5
        self.value= 20

class ImpToothSpear(Weapon):
    def __init__(self,name,damage,value):
        self.name="Imp Tooth Spear"
        self.damage=8
        self.value= 75

class DemonBoneShiv(Weapon):
    def __init__(self,name,damage,value):
        self.name="Demon Bone Shiv"
        self.damage=12
        self.value= 100


class DemonBoneAxe(Weapon):
    def __init__(self,name,damage,value):
        self.name="Demon Bone Axe"
        self.damage=18
        self.value= 500

class BrimstoneMace(Weapon):
    def __init__(self,name,damage,value):
        self.name="Brimstone Mace"
        self.damage=22
        self.value= 700

class RatlingDeathClaws(Weapon):
    def __init__(self,name,damage,value):
        self.name="Ratling Death Claws"
        self.damage=32
        self.value= 1200

class DoomHammer(Weapon):
    def __init__(self,name,damage,value):
        self.name="Doom Hammer"
        self.damage=37
        self.value= 1500

class SilverSword(Weapon):
    def __init__(self,name,damage,value):
        self.name="Silver Sword"
        self.damage=50
        self.value= 1500

class ShadowBlade(Weapon):
    def __init__(self,name,damage,value):
        self.name="Shadow Blade "
        self.damage=75
        self.value= 1500

class DemonBastardSword(Weapon):
    def __init__(self,name,damage,value):
        self.name="Demon Bastard Sword"
        self.damage=45
        self.value= 1500

class FacebreakerGauntlet(Weapon):
    def __init__(self,name,damage,value):
        self.name="FaceBreaker Gauntlet"
        self.damage=40
        self.value= 1500

class DoomKingSword(Weapon):
    def __init__(self,name,damage,value):
        self.name="Doom King Sword "
        self.damage=75
        self.value= 1500

class Armour():  
    def __init__(self):
        raise NotImplementedError("Do not create raw Armour Objects.")

    def __str__(self):
        return "{}+{} PROT ".format(self.name, self.protection)


class Rags(Armour):
    def __init__(self,name,protection,value):
        self.name="Rags"
        self.protection=0
        self.value= 20


class RatskinTunic(Armour):
    def __init__(self,name,protection,value):
        self.name="Ratskin Tunic"
        self.protection=3
        self.value= 75

class SilkArmour(Armour):
    def __init__(self,name,protection,value):
        self.name="Silk Armour"
        self.protection=7
        self.value= 100


class BrimstoneBoneArmour (Armour):
    def __init__(self,name,protection,value):
        self.name="Brimstone Bone Armour"
        self.protection=12
        self.value= 100

class HereticPlateMail (Armour):
    def __init__(self,name,protection,value):
        self.name="Heretic Plate Mail"
        self.protection=16
        self.value= 100

class ShadowArmour (Armour):
    def __init__(self,name,protection,value):
        self.name="Shadow Armour"
        self.protection=25
        self.value= 100

class HolyPlateMail (Armour):
    def __init__(self,name,protection,value):
        self.name="Holy Plate Mail"
        self.protection=35
        self.value= 100

class DoomKingPlateMail (Armour):
    def __init__(self,name,protection,value):
        self.name="Doom King Plate Mail"
        self.protection=50
        self.value= 100
