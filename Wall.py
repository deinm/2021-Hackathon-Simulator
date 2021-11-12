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
    def __init__(self, initial_position, target_position, width, height):
        super(DynamicWallSprite, self).__init__()
        black_wall = 255 * np.ones((width, height, 3))
        self.normal = pygame.surfarray.make_surface(black_wall)
        self.rect = pygame.Rect(self.normal.get_rect())
        self.initial_position = initial_position
        self.target_position = target_position
        self.rect.center = self.initial_position
        self.image = self.normal
        self.time = time.time()

    def update(self):
        elpased_time = (time.time() - self.time)
        tik = (int)(elpased_time * 100) % 200

        if  (int)(elpased_time % 8) < 2:
            self.rect.center = self.initial_position

        if  4<= (int)(elpased_time % 8) < 6: 
            self.rect.center = self.target_position    

        elif  2<=(int)(elpased_time % 8) < 4:
            self.rect.center = (self.initial_position[0] + (int)((self.target_position[0] - self.initial_position[0])*tik/200),\
                                 self.initial_position[1] + (int)((self.target_position[1] - self.initial_position[1])*tik/200))

        elif  6<=(int)(elpased_time % 8) < 8:
            self.rect.center = (self.target_position[0] - (int)((self.target_position[0] - self.initial_position[0])*tik/200),\
                                 self.target_position[1] - (int)((self.target_position[1] - self.initial_position[1])*tik/200))
        




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
