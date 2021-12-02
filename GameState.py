import pygame

import GameConfig
from GameConfig import *
from Worm import *
from Shoot import *

class GameState:
    def draw(self, window):
        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))
        window.blit(GameConfig.TERRAIN_IMG, (0, 0))
        window.blit(GameConfig.EAU_IMG, (0,0))

        self.worm.draw(window)
        self.worm2.draw(window)

        #self.Shoot.draw(window)


    def __init__(self):
        self.worm = Worm(20, GameConfig.MAP)
        self.worm2 = Worm(350, GameConfig.MAP)

        self.Shoot = Shoot(self.worm)

    def advance_state(self, next_move,window):
        self.worm.advance_state(next_move)
        self.Shoot.advance_state(next_move, window)

        if self.worm.is_touching(self.Shoot):
            if self.Shoot.Worm == self.worm2:
                print("touché worm 1")
                self.worm.hp -= 1
                print("hp worm 1 : "+str(self.worm.hp))
                self.Shoot.rect = pygame.Rect(30000,
                                              0,
                                              GameConfig.projectile_W,
                                              GameConfig.projectile_H)
        elif self.worm2.is_touching(self.Shoot):
            if self.Shoot.Worm == self.worm:
                print("touché worm 2")
                self.worm2.hp -= 1
                print("hp worm 2 : " + str(self.worm2.hp))
                self.Shoot.rect = pygame.Rect(30000,
                                0,
                                GameConfig.projectile_W,
                                GameConfig.projectile_H)
        elif self.Shoot.on_ground():
            self.Shoot.rect = pygame.Rect(30000,
                                          0,
                                          GameConfig.projectile_W,
                                          GameConfig.projectile_H)






    def angle(self,next_move):
        if next_move.angleHaut:
            GameConfig.ANGLE+=1
            print(GameConfig.ANGLE)
            if GameConfig.ANGLE>90:
                GameConfig.ANGLE = 90
        elif next_move.angleBas:
            GameConfig.ANGLE-=1
            print(GameConfig.ANGLE)
            if GameConfig.ANGLE<0:
                GameConfig.ANGLE = 0

    def puissance(self,next_move):
        if next_move.angleHaut:
            GameConfig.ANGLE+=1
            print(GameConfig.ANGLE)
            if GameConfig.ANGLE>90:
                GameConfig.ANGLE = 90
        elif next_move.angleBas:
            GameConfig.ANGLE-=1
            print(GameConfig.ANGLE)
            if GameConfig.ANGLE<0:
                GameConfig.ANGLE = 0

    def variationVecteur(self,next_move):

        if next_move.angle and GameConfig.D_DROIT==True:
            GameConfig.VECTEUR = pygame.math.Vector2(0,-GameConfig.PUISSANCE).rotate(GameConfig.ANGLE)
        elif next_move.angle and GameConfig.G_GAUCHE == True:
            GameConfig.VECTEUR = pygame.math.Vector2(0,-GameConfig.PUISSANCE).rotate(-GameConfig.ANGLE)



