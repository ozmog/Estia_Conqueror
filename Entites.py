from Arme import Arme
from Armure import Armure
from inventaire import Inventaire

class Entites(object):
    def __init__(self, arme = None, armure = None, level : int = 0, inventaire = Inventaire()) -> None:
        self.nom = ""

        # stats
        self.sante = 100
        self.sante_max = 100
        self.force = 10
        self.technique = 10
        self.defense = 10
        self.distance_attaque = 75
        self.race = None

        #
        self.arme = arme
        self.armure = armure
        self.inventaire = inventaire
        self.position = [0, 0]
        self.taille = 50
        self.vitesse = 6

        # argent et experience
        self.xp = 0
        self.xp_neccessaire = 5
        self.level = level
        self.coins = 0
        self.diamants = 0
        self.xp_drop = 0

        # skin de base 
        self.img_psL = "player\player with bg\player_standing_L.png"
        self.img_psR = "player\player with bg\player_standing_R.png"
        self.img_psL_running_1 = "player\player with bg\player_standing_L_running_1.png"
        self.img_psL_running_2 = "player\player with bg\player_standing_L_running_2.png"
        self.img_psR_running_1 = "player\player with bg\player_standing_R_running_1.png"
        self.img_psR_running_2 = "player\player with bg\player_standing_R_running_2.png"
        self.player_img_affiché = "player\player with bg\player_standing_L.png"


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
        if abs(self.position[0] - ennemi.position[0]) <= self.distance_attaque and abs(self.position[1] - ennemi.position[1]) <= self.distance_attaque :
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
        
        
