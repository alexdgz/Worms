import pygame
from Worm import *
import numpy as np
from GameConfig import *



class Shoot:
    def __init__(self, Worm):
        self.Worm = Worm

        self.rect = pygame.Rect(Worm.rect.right,
                                Worm.rect.top,
                                GameConfig.projectile_W,
                                   GameConfig.projectile_H)
        self.vx = 1
        self.vy = -7
        self.image = GameConfig.PROJECTILE_IMG

    def draw(self,window):
        window.blit(self.image, self.rect.topleft)

    def on_ground(self):
        if self.rect.bottom == GameConfig.Y_PLATEFORM:
            return True
        return False

    def fg(t,y):
        return np.array([0,-GameConfig.GRAVITY/GameConfig.MASSE,y[0],y[1]])

    #y = np.array([2,2,50,50])
    def euler(y,h,t):
        return y + h * Shoot.fg(t,y)

    def advance_state(self, next_move,window):
        if next_move.shoot:
            self.rect.left=self.Worm.rect.left
            self.draw(window)

            y = np.array([self.vx,self.vy,self.rect.left,self.rect.top])
            print(y)

            for i in range(10):
                y = Shoot.euler(y,20,2)
                print(y)

