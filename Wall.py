import pygame
import numpy as np
import time



class WallSprite(pygame.sprite.Sprite):

    def __init__(self, position, width, height):
        super(WallSprite, self).__init__()
        black_wall = 255 * np.ones((width, height, 3))
        self.normal = pygame.surfarray.make_surface(black_wall)
        self.rect = pygame.Rect(self.normal.get_rect())
        self.rect.center = position
        self.image = self.normal

    def update(self):
        pass

class DynamicWallSprite(pygame.sprite.Sprite):
    def __init__(self, position, width, height):
        super(DynamicWallSprite, self).__init__()
        black_wall = 255 * np.ones((width, height, 3))
        self.normal = pygame.surfarray.make_surface(black_wall)
        self.rect = pygame.Rect(self.normal.get_rect())
        self.initial_position = position
        self.rect.center = position
        self.image = self.normal
        self.time = time.time()
    def update(self):
        
        if (int)(time.time() - self.time) % 2 == 1:
            self.rect.center = (-1000,-1000)
        else:
            self.rect.center = self.initial_position
        pass




class invisible_WallSprite(pygame.sprite.Sprite):
    def __init__(self, position, width, height):
        super(invisible_WallSprite, self).__init__()
        black_wall = 0 * np.ones((width, height, 3))
        self.normal = pygame.surfarray.make_surface(black_wall)
        self.rect = pygame.Rect(self.normal.get_rect())
        self.rect.center = position
        self.image = self.normal

    def update(self):
        pass


if __name__ == "__main__":
    pygame.init()
    w = WallSprite((10, 2), 1, 1)
