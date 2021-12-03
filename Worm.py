import pygame

import Platform
from GameConfig import *
from Platform import *

#classe pour définir notre worms
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
        self.hp = 3

    # méthode pour afficher le worm
    def draw(self,window):
        window.blit(self.image, self.rect.topleft)

    # méthode pour vérifier si le worm est sur le sol
    def on_ground(self):
        return pygame.sprite.collide_mask(self, Platform(0))
    # méthode pour vérifier que le projectile touche le worm
    def is_touching(self,projectile):
        return pygame.sprite.collide_mask(self,projectile)

    # méthode pour avancé dans les différents états du worm
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
        # Calcul de vitesse
        self.vx = fx*GameConfig.DT
        # Vérification si le worm est sur le sol
        if self.on_ground():
            self.vy = fy * GameConfig.DT
        else:
            self.vy = self.vy + GameConfig.GRAVITY * GameConfig.DT
        # Calcul de position
        x = self.rect.left
        vx_min = -x / GameConfig.DT
        vx_max = (GameConfig.WINDOW_L - GameConfig.WORM_L - x) / GameConfig.DT
        self.vx = min(self.vx, vx_max)
        self.vx = max(self.vx, vx_min)
        y = self.rect.top
        vy_max = (GameConfig.Y_PLATEFORM - GameConfig.WORM_H - y) / GameConfig.DT
        self.vy = min(self.vy, vy_max)
        self.rect = self.rect.move(self.vx * GameConfig.DT, self.vy * GameConfig.DT)
