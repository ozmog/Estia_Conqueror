from Entites import Entites
       
class Gobelin(Entites):
    def __init__(self):
        Entites.__init__(self)
        self.force=5
    
class Squelette(Entites):
    def __init__(self):
        Entites.__init__(self)
        self.nom_classe = "sqeulette"
    
class Orc(Entites):
    def __init__(self):
        Entites.__init__(self)
        self.nom_classe = "Orc"
        self.sante_max = 150
        self.defense = 15
        self.force = 7
    
class Vampire(Entites):
    def __init__(self):
        Entites.__init__(self)
        self.nom_classe = "Vampire"
        self.sante_max = 80
    
class Elf_noir(Entites):
    def __init__(self):
        Entites.__init__(self)
        self.nom_classe = "Elf Noir"
        self.sante= 75
        
class centaure(Entites):
    def __init__(self):
        Entites.__init__(self)
        self.nom_classe = ""
        self.distance_attaque = 5