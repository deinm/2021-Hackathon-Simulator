import pygame
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT, K_w, K_a, K_s, K_d


class Control:
    def __init__(self, player=1):
        if player == 1:
            keys = [K_UP, K_DOWN, K_RIGHT, K_LEFT]
        elif player == 2:
            keys = [K_w, K_s, K_d, K_a]

        self.up_event =\
            pygame.event.Event(pygame.USEREVENT, {'key': keys[0]})
        self.down_event =\
            pygame.event.Event(pygame.USEREVENT, {'key': keys[1]})
        self.right_event =\
            pygame.event.Event(pygame.USEREVENT, {'key': keys[2]})
        self.left_event =\
            pygame.event.Event(pygame.USEREVENT, {'key': keys[3]})

    def up(self):
        try:
            pygame.event.post(self.up_event)
        except pygame.error:
            pass

    def down(self):
        try:
            pygame.event.post(self.down_event)
        except pygame.error:
            pass

    def right(self):
        try:
            pygame.event.post(self.right_event)
        except pygame.error:
            pass

    def left(self):
        try:
            pygame.event.post(self.left_event)
        except pygame.error:
            pass
