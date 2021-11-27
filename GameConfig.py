import pygame

from Map import *

class GameConfig:
    #définition de la fenetre
    WINDOW_H = 640
    WINDOW_L = 960

    def init():
        GameConfig.BACKGROUND_IMG =pygame.image.load('ressources/background.png')
        GameConfig.CRAPOUX_IMG = pygame.image.load('ressources/crapoux_asset.png')
        Map.mapCreate()
        GameConfig.TERRAIN_IMG = pygame.image.load('ressources/terrain_asset.png')
        GameConfig.PROJECTILE_IMG = pygame.image.load('ressources/projectile.png')


    #définition TEMPORAIRE de la plateforme
    Y_PLATEFORM = 516
    GRAVITY = 9.81
    MASSE = 30

    #définition du personnage
    WORM_H = 64
    WORM_L = 49
    DT = 0.5
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT
    FORCE_JUMP = -100

    #définition du projectile
    projectile_H = 10
    projectile_W = 10
    PUISSANCE = 3
    ANGLE = 45

