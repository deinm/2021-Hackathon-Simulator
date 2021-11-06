import pygame
import random as rd
from V2X import V2X

class TrophySprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/trophy.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.position_dict = {
            1 : [(930, 15),(930, 115),(930, 265),(930, 415),(930, 615),(930, 715)],
            2 : [(10, 15),(10, 315),(10, 515),(10, 715)],
            3 : [(470, 15),(470, 375),(570, 220),(700, 515),(240, 220),(400, 615),(470, 715)],
        }
        self.rect.x, self.rect.y = (470, 375)
        self.idx = None
        V2X.__init__(self, (self.rect.x, self.rect.y), name="Trophy")
        self.data = [self.name, (self.rect.x, self.rect.y)]

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def trophy_respawn(self):  
        rd_idx_list = list(self.position_dict.keys())
        if self.idx is not None:
            rd_idx_list.remove(self.idx)
        self.idx = rd.choice(rd_idx_list)
        self.rect.x, self.rect.y = rd.choice(self.position_dict[self.idx])
        self.update()

    def update(self):
        self.data = [self.name,(self.rect.x, self.rect.y)]