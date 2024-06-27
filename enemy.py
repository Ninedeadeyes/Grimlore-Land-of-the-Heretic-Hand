
class Enemy():    
    def __init__(self,name,strength,hp,xp,gold,item,special):
        self.name=name
        self.strength=strength
        self.hp=hp
        self.xp=xp
        self.gold=gold
        self.item=item
        self.special=special
        
    def __str__(self):
        return f"{self.name}"     # Not used in game yet but will be useful if I ever create a bestiary for the game 


#Random Event enemies 

class BogImp  (Enemy):
    def __init__(self,name="Bog Imp",strength=1,hp=80,xp=20,gold=25,item="Imp Tooth",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class Ratling  (Enemy):
    def __init__(self,name="Ratling",strength=2,hp=80,xp=30,gold=30,item="Ratling Fur",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class LesserDemon (Enemy):
    def __init__(self,name="Lesser Demon",strength=4,hp=100,xp=40,gold=35,item="Demon Bone",special="bloodlust"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class HellHound  (Enemy):
    def __init__(self,name="Hell Hound",strength=15,hp=180,xp=350,gold=150,item="Demon Bone",special="bloodlust"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class RatlingMage(Enemy):
    def __init__(self,name="Ratling Mage",strength=20,hp=250,xp=350,gold=200,item="Ratling Fur",special="drain"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class RedEttercap  (Enemy):
    def __init__(self,name="Red Ettercap",strength=15,hp=300,xp=350,gold=300,item="Demon Silk",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class DoomSpeaker (Enemy):
    def __init__(self,name="Doom Speaker",strength=50,hp=350,xp=1000,gold=1200,item="Demon Silk",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class HandofUngas (Enemy):
    def __init__(self,name="Hand of Ungas",strength=35,hp=550,xp=1000,gold=1200,item="Brimstone",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class DeathBloom(Enemy):
    def __init__(self,name="Death Bloom ",strength=45,hp=550,xp=1200,gold=1500,item="Demon Silk",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

#BOSS 

class SeaBeast (Enemy):
    def __init__(self,name="Sea Beast",strength=20,hp=700,xp=500,gold=200,item="Demon Bone",special="heal1"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class DoomKing (Enemy):
    def __init__(self,name="Doom King",strength=72,hp=3000,xp=10000,gold=1000000,item="Demon Bone",special="heal2"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class ShadowHunter (Enemy):
    def __init__(self,name="Shadow Hunter",strength=50,hp=400,xp=700,gold=300,item="nothing",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)
    
class Butcher(Enemy):
    def __init__(self,name="Butcher",strength=40,hp=700,xp=1000,gold=500,item="Demon Bone",special="bloodlust"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class BloodPitChampion(Enemy):
    def __init__(self,name="Blood Pit Champion",strength=78,hp=1000,xp=2000,gold=2000,item="nothing",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class BlackDragon(Enemy):
    def __init__(self,name="Black Dragon",strength=65,hp=600,xp=1200,gold=2000,item="Demon Bone",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)
    
class DeathKnight(Enemy):
    def __init__(self,name="Death Knight",strength=70,hp=550,xp=1200,gold=2000,item="Demon Bone",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

 #Dungeons

class Mimic(Enemy):
    def __init__(self,name="Mimic",strength=8,hp=100,xp=60,gold=50,item="nothing",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class GreaterMimic(Enemy):
    def __init__(self,name="Greater Mimic",strength=25,hp=220,xp=350,gold=50,item="nothing",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class DemonicMimic(Enemy):
    def __init__(self,name="Demonic Mimic",strength=50,hp=250,xp=500,gold=500,item="nothing",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)
    
class BrimstoneGremlin (Enemy):
    def __init__(self,name="Brimstone Gremlin",strength=6,hp=100,xp=50,gold=40,item="Brimstone",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class FallenKnight(Enemy):
    def __init__(self,name="Fallen Knight",strength=7,hp=140,xp=80,gold=50,item="Iron Shard",special="drain"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class Ettercap(Enemy):
    def __init__(self,name="Ettercap",strength=10,hp=120,xp=100,gold=60,item="Demon Silk",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class DemonTroll(Enemy):
    def __init__(self,name="Demon Troll",strength=16,hp=200,xp=120,gold=60,item="Demon Bone",special="bloodlust"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class ChaosSpider(Enemy):
    def __init__(self,name="Chaos Spider",strength=16,hp=150,xp=200,gold=90,item="Demon Silk",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class IronTuskDemon(Enemy):
    def __init__(self,name="Iron Tusk Demon",strength=18,hp=350,xp=300,gold=150,item="Iron Shard",special="bloodlust"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)
    
class CorruptedIronGolem(Enemy):
    def __init__(self,name="Corrupted Iron Golem",strength=14,hp=400,xp=250,gold=120,item="Iron Shard",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class RatlingAssassin (Enemy):
    def __init__(self,name="Ratling Assassin",strength=25,hp=120,xp=250,gold=250,item="Ratling Fur",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class DemonicAbomination (Enemy):
    def __init__(self,name="Demonic Abomination",strength=22,hp=240,xp=300,gold=200,item="Demon Bone",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)
    
class LunaticCultist(Enemy):
    def __init__(self,name="Lunatic Cultist",strength=14,hp=180,xp=150,gold=80,item="Brimstone",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class ChaosSpawn(Enemy):
    def __init__(self,name="Chaos Spawn",strength=16,hp=150,xp=150,gold=100,item="Brimstone",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class CultistChampion(Enemy):
    def __init__(self,name="Cultist Champion",strength=20,hp=250,xp=300,gold=200,item="Demon Bone",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)
    
class CultistImpaler(Enemy):
    def __init__(self,name="Cultist Impaler",strength=30,hp=300,xp=400,gold=400,item="Demon Bone",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class GreaterDemon(Enemy):
    def __init__(self,name="Greater Demon",strength=40,hp=250,xp=700,gold=750,item="Demon Bone",special="bloodlust"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class PlagueDemon (Enemy):
    def __init__(self,name="Plague Demon",strength=25,hp=400,xp=400,gold=750,item="Demon Bone",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)
    
class DemonWarChampion(Enemy):
    def __init__(self,name="Demon War Champion",strength=45,hp=400,xp=1000,gold=1000,item="Demon Bone",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class ClockworkHorror (Enemy):
    def __init__(self,name="Clockwork Horror",strength=60,hp=120,xp=600,gold=750,item="Iron Shard",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)

class ClockworkPainTaker (Enemy):
    def __init__(self,name="Clockwork Pain Taker ",strength=30,hp=600,xp=900,gold=750,item="Iron Shard",special="heal1"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)
    
class ClockworkEngineer(Enemy):
    def __init__(self,name="Clockwork Engineer",strength=40,hp=400,xp=800,gold=1000,item="Iron Shard",special="nothing"):
        Enemy.__init__(self,name,strength,hp,xp,gold,item,special)
