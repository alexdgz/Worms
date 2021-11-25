import pygame
from GameConfig import *
from Worm import *
from Shoot import *

class GameState:
    def draw(self, window):
        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))
        self.worm.draw(window)
        #self.Shoot.draw(window)


    def __init__(self):
        self.worm = Worm(20)
        self.Shoot = Shoot(self.worm)

    def advance_state(self, next_move,window):
        self.worm.advance_state(next_move)
        self.Shoot.advance_state(next_move,window)