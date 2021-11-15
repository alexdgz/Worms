import pygame
from GameConfig import *


class GameState:
    def draw(self, window):
        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))