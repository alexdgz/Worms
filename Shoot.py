import pygame
from Worm import *
import numpy as np
from GameConfig import *



class Shoot:
    def __init__(self, Worm):
        self.Worm = Worm

        self.rect = pygame.Rect(Worm.rect.left,
                                Worm.rect.top,
                                GameConfig.projectile_W,
                                   GameConfig.projectile_H)
        self.vx = 5
        self.vy = -10
        self.image = GameConfig.PROJECTILE_IMG

    def draw(self,window):
        window.blit(self.image, self.rect.topleft)

    def on_ground(self):
        if self.rect.bottom == GameConfig.Y_PLATEFORM:
            return True
        return False

    def fg(self,y):
        return np.array([0,GameConfig.GRAVITY/GameConfig.MASSE,y[0],y[1]])

    def euler(self,y,h,t,f):

        #T = np.array([t])
        #T = T[0] + h

        Y = y
        #print(T[0])
        Y = Y + h * f(Y)

        return Y

    def advance_state(self, next_move,window):
        if next_move.shoot:
            self.draw(window)

            while(self.rect.top<GameConfig.Y_PLATEFORM):
                pygame.time.wait(10)
                self.draw(window)

                t = 0;
                y = np.array([self.vx,self.vy,self.rect.left,self.rect.top])

                Y = self.euler(y,GameConfig.DT,t,self.fg)

                self.vx = Y[0]
                self.vy = Y[1]

                self.rect = self.rect.move(Y[2]-self.rect.left,Y[3]-self.rect.top)

                self.rect.left = Y[2]
                self.rect.top = Y[3]





