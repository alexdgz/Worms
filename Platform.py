import pygame
from GameConfig import *
class Platform(pygame.sprite.Sprite):
    def __init__(self,x):
        self.rect = pygame.Rect(x,
                                0,
                                GameConfig.WINDOW_L,
                                GameConfig.WINDOW_H)
        self.vx = 0
        self.vy = 0
        self.image = GameConfig.TERRAIN_IMG
        self.mask = GameConfig.TERRAIN_MASK