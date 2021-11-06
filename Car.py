import pygame
import math
import inspect
import sys
import platform
import os

from pygame.locals import (K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP,
                           KEYDOWN, USEREVENT, K_w, K_a, K_s, K_d)

from Authority import AuthorityExecption


class CarSprite(pygame.sprite.Sprite):
    __MAX_FORWARD_SPEED = 15
    __MAX_REVERSE_SPEED = 15

    def __init__(self, image, position, direction=0, player=1):
        pygame.sprite.Sprite.__init__(self)
        self.__src_image = pygame.image.load(image)
        self.car_image = pygame.image.load(image)
        self.__position = position
        self.__speed = 0
        self.__k_left = self.__k_right = self.__k_down = self.__k_up = 0
        self.__direction = direction
        self.player = player
        self.event_keys = [K_RIGHT, K_LEFT, K_UP, K_DOWN]
        self.initial_direction = direction
        self.initial_position = position
        self.last_collision = 999
        if player == 2:
            self.event_keys = [K_d, K_a, K_w, K_s]
        self.update()

    def update(self, deltat=False):
        # SIMULATION
        self.__speed += (self.__k_up + self.__k_down)
        if self.__speed > self.__MAX_FORWARD_SPEED:
            self.__speed = self.__MAX_FORWARD_SPEED
        if self.__speed < -self.__MAX_REVERSE_SPEED:
            self.__speed = -self.__MAX_REVERSE_SPEED
<<<<<<< Updated upstream
        if self.__speed != 0:
=======
        if self.__speed == 0:
            pass
        else:
>>>>>>> Stashed changes
            self.__direction += (self.__k_right + self.__k_left)
            self.__direction = self.__direction % 360
        x, y = (self.__position)
        rad = self.__direction * math.pi / 180
        x += -self.__speed*math.sin(rad)
        y += -self.__speed*math.cos(rad)
        self.__position = (x, y)
        self.image =\
            pygame.transform.rotate(self.__src_image, self.__direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.__position
    
    def respawn(self):
        self.__speed = 0
        self.__direction = self.initial_direction
        self.__k_left = self.__k_right = self.__k_down = self.__k_up = 0
        self.__position = self.initial_position        
        self.__src_image = self.car_image
        self.last_collision = 999
        self.update()
    
    def crash(self, collide_seconds: int, crash_image):
        self.__src_image = crash_image
        self.last_collision = collide_seconds
        self.update()

    @property
    def MAX_FORWARD_SPEED(self):
        return self.__MAX_FORWARD_SPEED

    @property
    def MAX_REVERSE_SPEED(self):
        return self.__MAX_REVERSE_SPEED

    @property
    def speed(self):
        return self.__speed

    @property
    def position(self):
        return self.__position

    @property
    def direction(self):
        return self.__direction

    @property
    def k_up(self):
        return self.__k_up

    @property
    def k_down(self):
        return self.__k_down

    @property
    def k_right(self):
        return self.__k_right

    @property
    def k_left(self):
        return self.__k_left

    @k_up.setter
    def k_up(self, new_k_up):
        if inspect.stack()[1][1].split(os.sep)[-1] == 'Game.py':
            self.__k_up = new_k_up
        else:
            sys.tracebacklimit = 0
            print("YOU ARE TRYING TO CHEAT!")
            raise AuthorityExecption('Not allowed File %s is trying to \
                change CarSprite.k_up at \'%s\'' % (
                    inspect.stack()[1][1].split(os.sep)[-1],
                    inspect.stack()[1][0])
                    )

    @k_down.setter
    def k_down(self, new_k_down):
        if inspect.stack()[1][1].split(os.sep)[-1] == 'Game.py':
            self.__k_down = new_k_down
        else:
            sys.tracebacklimit = 0
            print("YOU ARE TRYING TO CHEAT!")
            raise AuthorityExecption('Not allowed File %s is trying to \
                change CarSprite.k_up at \'%s\'' % (
                    inspect.stack()[1][1].split(os.sep)[-1],
                    inspect.stack()[1][0])
                    )

    @k_right.setter
    def k_right(self, new_k_right):
        if inspect.stack()[1][1].split(os.sep)[-1] == 'Game.py':
            self.__k_right = new_k_right
        else:
            sys.tracebacklimit = 0
            print("YOU ARE TRYING TO CHEAT!")
            raise AuthorityExecption('Not allowed File %s is trying to \
                change CarSprite.k_up at \'%s\'' % (
                    inspect.stack()[1][1].split(os.sep)[-1],
                    inspect.stack()[1][0])
                    )

    @k_left.setter
    def k_left(self, new_k_left):
        if inspect.stack()[1][1].split(os.sep)[-1] == 'Game.py':
            self.__k_left = new_k_left
        else:
            sys.tracebacklimit = 0
            print("YOU ARE TRYING TO CHEAT!")
            raise AuthorityExecption('Not allowed File %s is trying to \
                change CarSprite.k_up at \'%s\'' % (
                    inspect.stack()[1][1].split(os.sep)[-1],
                    inspect.stack()[1][0])
                    )

    @MAX_FORWARD_SPEED.setter
    def MAX_FORWARD_SPEED(self, new_MAX_FORWARD_SPEED):
        if inspect.stack()[1][1].split(os.sep)[-1] == 'Game.py':
            self.__MAX_FORWARD_SPEED = new_MAX_FORWARD_SPEED
        else:
            sys.tracebacklimit = 0
            print("YOU ARE TRYING TO CHEAT!")
            raise AuthorityExecption('Not allowed File %s is trying to \
                change CarSprite.k_up at \'%s\'' % (
                    inspect.stack()[1][1].split(os.sep)[-1],
                    inspect.stack()[1][0])
                    )

    @MAX_REVERSE_SPEED.setter
    def MAX_REVERSE_SPEED(self, new_MAX_REVERSE_SPEED):
        if inspect.stack()[1][1].split(os.sep)[-1] == 'Game.py':
            self.__MAX_REVERSE_SPEED = new_MAX_REVERSE_SPEED
        else:
            sys.tracebacklimit = 0
            print("YOU ARE TRYING TO CHEAT!")
            raise AuthorityExecption('Not allowed File %s is trying to \
                change CarSprite.k_up at \'%s\'' % (
                    inspect.stack()[1][1].split(os.sep)[-1],
                    inspect.stack()[1][0])
                    )