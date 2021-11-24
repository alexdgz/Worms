import pygame

class GameConfig:
    #définition de la fenetre
    WINDOW_H = 640
    WINDOW_L = 960

    def init():
        GameConfig.BACKGROUND_IMG =pygame.image.load('ressources/background.png')
        GameConfig.CRAPOUX_IMG = pygame.image.load('ressources/crapoux_asset.png')

    #définition TEMPORAIRE de la plateforme
    Y_PLATEFORM = 516

    #définition du personnage
    WORM_H = 64
    WORM_L = 49
    DT = 0.5
    FORCE_LEFT = -20
    FORCE_RIGHT = -FORCE_LEFT
    GRAVITY = 9.81
    FORCE_JUMP = -100

