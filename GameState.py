import pygame
from GameConfig import *
from Worm import *
from Shoot import *

class GameState:
    def draw(self, window):
        window.blit(GameConfig.BACKGROUND_IMG, (0, 0))
        window.blit(GameConfig.TERRAIN_IMG, (0, 0))
        self.worm.draw(window)

        #self.Shoot.draw(window)


    def __init__(self):
        self.worm = Worm(20)
        self.Shoot = Shoot(self.worm)

    def advance_state(self, next_move,window):
        self.worm.advance_state(next_move)
        self.Shoot.advance_state(next_move,window)




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



