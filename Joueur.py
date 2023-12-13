import pygame
class Player(pygame.sprite.Sprite):
    
    # Fonction d'initiation du sprite

    def __init__(self):
        super().__init__()

        # Chargement de l'image de base :
        self.image_droite = pygame.image.load("Images/Astronaute_cote_droit.png").convert_alpha()
        self.image_gauche = pygame.image.load("Images/Astronaute_cote_gauche.png").convert_alpha()
        self.image_x = 57
        self.image_y = 118
        self.image = pygame.transform.scale(self.image_droite,(self.image_x,self.image_y))
        
        # Defini la taille du sprite par / a l'image :
        self.rect = self.image.get_rect()

        # Position image / sprite :
        self.rect.x = 0
        self.rect.y = 770
