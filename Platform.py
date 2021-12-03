import pygame
from GameConfig import *
class Platform(pygame.sprite.Sprite):#cette classe permet de gérer la map créée dans Map.py en temps que sprite et donc de pouvoir utiliser les masks
    def __init__(self,x):
        self.rect = pygame.Rect(x,
                                0,
                                GameConfig.WINDOW_L,
                                GameConfig.WINDOW_H)
        self.vx = 0
        self.vy = 0
        self.image = GameConfig.TERRAIN_IMG
        self.mask = GameConfig.TERRAIN_MASK