from Arme import Arme
from Armure import Armure

class Entites(object):
    def __init__(self, arme = Arme("mains"), armure = Armure(), level : int = 0) -> None:
        self.nom = ""
        self.sante = 100
        self.sante_max = 100
        self.force = 10
        self.technique = 10
        self.defence = 10
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

    def level_up(self):
        if self.xp_neccessaire == self.xp:
            self.xp = 0
            self.level += 1
            self.xp_neccessaire = int((self.xp_neccessaire * 1.2 + 12) // 1)
            return True
        return False
    
