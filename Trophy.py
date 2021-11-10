import os
import json
import pygame
import random as rd

from V2X import V2X


class TrophySprite(pygame.sprite.Sprite):
    def __init__(self, map_idx):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/trophy.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()

        # load trophy position from file.
        position_filename = os.path.join("trophies", f"trophies{map_idx}.json")
        with open(position_filename, "r") as f:
            self.position_dict = json.load(f)
        self.rect.x, self.rect.y = [320, 360]
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
        self.data = [self.name, (self.rect.x, self.rect.y)]
