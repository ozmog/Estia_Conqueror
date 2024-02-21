from Arme import Arme
from Armure import Armure

class Entites(object):
    def __init__(self, arme = None, armure = None, level : int = 0) -> None:
        self.nom = ""
        self.sante = 100
        self.sante_max = 100
        self.force = 10
        self.technique = 10
        self.defense = 10
        self.race = None
        self.taille_inventaire = 5
        self.inventaire = [None for i in range(self.taille_inventaire)]
        self.position = [0, 0, 0]
        self.xp = 0
        self.level = level
        self.xp_neccessaire = 5
        self.arme = arme
        self.armure = armure
        self.coins = 0
        self.diamants = 0
        self.xp_drop = 0

    def en_vie(self):
        if self.sante <= 0:
            return False
        return True
    
    def level_up(self):
        if self.xp_neccessaire == self.xp:
            self.xp = 0
            self.level += 1
            self.xp_neccessaire = int((self.xp_neccessaire * 1.2 + 12) // 1)
            self.sante_max += 5
            self.sante += 5
            n = input("1 : augmenter la force\n2 : augmenter defense")
            if n == 1 or n == "force" or n == "augmenter la force":
                return True
        return False
    
    def attaque(self, ennemi):
        ennemi.sante -= (self.force + self.arme.degats) - ennemi.armure.defense
        self.arme.durabilités -= 1
        if ennemi.sante <= 0:
            if self.race == "vampire":
                self.sante += (self.sante_max/100)*10
                if self.sante < self.sante_max:
                    self.sante = self.sante_max
            ennemi.mort = True
            self.xp += ennemi.xp_drop*2 if self.race == "goblin" else ennemi.xp_drop
            self.level_up()
        
        
