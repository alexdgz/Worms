import numpy as np
from PIL import Image
import pygame
from Worm import *




class Map(pygame.sprite.Sprite):
    def __init__(self, x, GameConfig):
        self.rect = pygame.Rect(x,
                                0,
                                GameConfig.WINDOW_L,
                                GameConfig.WINDOW_H)
        self.vx = 0
        self.vy = 0
        self.image = GameConfig.TERRAIN_IMG
        self.mask = GameConfig.TERRAIN_MASK

    def is_touching(self, Worm):
        return pygame.sprite.collide_mask(self,Worm)
