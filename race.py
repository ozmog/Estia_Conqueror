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
    
class Vampire(Entites):
    def __init__(self):
        Entites.__init__(self)
        self.nom_classe = "Vampire"
    
class Elf_noir(Entites):
    def __init__(self):
        Entites.__init__(self)
        self.nom_classe = "Elf Noir"
        
class centaure(Entites):
    def __init__(self):
        Entites.__init__(self)
        self.nom_classe = ""