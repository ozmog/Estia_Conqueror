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
        self.nom_skin = ""
        self.coins = 0
        self.diamants = 0

    def en_vie(self):
        if self.sante <= 0:
            return False
        return True
    
    def level_up(self):
        if self.xp_neccessaire == self.xp:
            self.xp = 0
            self.level += 1
            self.xp_neccessaire = int((self.xp_neccessaire * 1.2 + 12) // 1)
            return True
        return False
    
    def attaque(self, ennemi):
        ennemi.sante -= (self.force + self.arme.degats) // self.armure.defense
        self.arme.durabilités -= 1
        if ennemi.sante <= 0:
            if self.race == "vampire":
                self.sante += 5
                if self.sante < 80:
                    self.sante = 80
            ennemi.mort = True
            self.xp += 5 if self.race == "goblin" else 2
            if self.xp <= 20:
                self.xp -= 20
                self.lvl += 1
                self.force += 2
        
        
