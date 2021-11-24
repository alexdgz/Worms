import pygame
from GameConfig import *
from Worm import *


class GameState:
    def draw(self, window):
        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))
        self.worm.draw(window)

    def __init__(self):
        self.worm = Worm(20)

    def advance_state(self, next_move):
        self.worm.advance_state(next_move)