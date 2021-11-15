# import des modules et des autres fichiers
import pygame
from GameConfig import *
from GameState import *

def game_loop(window):

    quitting = False
    game_state = GameState()
    while not quitting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True

def main():
    pygame.init()
    GameConfig.init()
    window = pygame.display.set_mode((GameConfig.WINDOW_L, GameConfig.WINDOW_H))
    pygame.display.set_caption("VR de Terre.exe")
    game_loop()
    pygame.quit()
    quit()

main()