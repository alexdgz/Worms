import pygame

class GameConfig:
    #définition de la fenetre
    WINDOW_H = 544
    WINDOW_L = 735

    def init():
        GameConfig.BACKGROUND_IMG =pygame.image.load('ressources/background.jpg')

    #définition TEMPORAIRE de la plateforme
    PLATEFORM_Y = 504