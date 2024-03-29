import pygame
from Worm import *
import numpy as np
from GameConfig import *

class Shoot(pygame.sprite.Sprite):
    def __init__(self, Worm):#création du projectile affecté a un worm
        self.Worm = Worm

        self.rect = pygame.Rect(Worm.rect.left,
                                Worm.rect.top,
                                GameConfig.projectile_W,
                                   GameConfig.projectile_H)
        self.vx = 5
        self.vy = -10
        self.image = GameConfig.PROJECTILE_IMG
        self.mask = GameConfig.PROJECTILE_MASK


    def draw(self,window):#fonction pour visualiser le projectile
        window.blit(self.image, self.rect.topleft)

    def on_ground(self):#fonction qui revoie true quand le projectile touche le sol de la map
        if pygame.sprite.collide_mask(self,Platform(0)):
            print("on ground")
            return True
        return False

    def fg(self,y):# calcule de f pour euler
        return np.array([0,GameConfig.GRAVITY/GameConfig.MASSE,y[0],y[1]])

    def euler(self,y,dt,f): # calcule de euler
        return y + dt * f(y)


    def advance_state(self, next_move,window):

        if next_move.shoot:

               self.draw(window)
               y = np.array([GameConfig.VECTEUR.x, GameConfig.VECTEUR.y, self.rect.left, self.rect.top])
               Y = self.euler(y,GameConfig.DT,self.fg)
                # redéfinition des vecteur avec les nouveaux calculés
               GameConfig.VECTEUR.x = Y[0]
               GameConfig.VECTEUR.y = Y[1]
               #redefinition de la position du projectile
               self.rect = self.rect.move(Y[2]-self.rect.left,Y[3]-self.rect.top)
               self.rect.left = Y[2]
               self.rect.top = Y[3]