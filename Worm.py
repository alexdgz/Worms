import pygame

import Platform
from GameConfig import *
from Platform import *

class Worm(pygame.sprite.Sprite) :
    def __init__(self, x, map):
        self.rect = pygame.Rect(x,
                                GameConfig.Y_PLATEFORM - GameConfig.WORM_H,
                                GameConfig.WORM_L,
                                GameConfig.WORM_H)
        self.vx = 0
        self.vy = 0
        self.image = GameConfig.CRAPOUX_IMG
        self.mask = GameConfig.CRAPOUX_MASK
        self.map = map


    def draw(self,window):
        window.blit(self.image, self.rect.topleft)


    def on_ground(self):
        return pygame.sprite.collide_mask(self, Platform(0))

    def is_touching(self,projectile):
        return pygame.sprite.collide_mask(self,projectile)


    def advance_state(self, next_move):

        # Acceleration
        fx = 0
        fy = 0
        if next_move.left:
            fx = GameConfig.FORCE_LEFT
        elif next_move.right:
            fx = GameConfig.FORCE_RIGHT
        elif next_move.jump:
            fy = GameConfig.FORCE_JUMP
        # Vitesse
        self.vx = fx*GameConfig.DT

        if self.on_ground():
            self.vy = fy * GameConfig.DT
        else:
            self.vy = self.vy + GameConfig.GRAVITY * GameConfig.DT
        # Position
        x = self.rect.left
        vx_min = -x / GameConfig.DT
        vx_max = (GameConfig.WINDOW_L - GameConfig.WORM_L - x) / GameConfig.DT
        self.vx = min(self.vx, vx_max)
        self.vx = max(self.vx, vx_min)
        y = self.rect.top
        vy_max = (GameConfig.Y_PLATEFORM - GameConfig.WORM_H - y) / GameConfig.DT
        self.vy = min(self.vy, vy_max)
        self.rect = self.rect.move(self.vx * GameConfig.DT, self.vy * GameConfig.DT)

        """
        if(self.on_ground()):
            self.rect=self.rect.move(0,self.map.lagrange(self.rect.midbottom[0])+10)
        """