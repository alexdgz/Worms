# import des modules et des autres fichiers
from GameState import *
from Move import *
from GameConfig import *
import pygame

def game_loop(window):

    quitting = False
    game_state = GameState()
    game_state.draw(window)
    while not quitting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
        next_move = get_next_move()
        game_state.draw(window)
        pygame.time.delay(10)
        game_state.advance_state(next_move)
        pygame.display.update()

def get_next_move():
    next_move = Move()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        next_move.right = True
    if keys[pygame.K_LEFT]:
        next_move.left = True
    if keys[pygame.K_UP]:
        next_move.jump = True
    return next_move


def main():
    pygame.init()
    GameConfig.init()
    window = pygame.display.set_mode((GameConfig.WINDOW_L, GameConfig.WINDOW_H))
    pygame.display.set_caption("VR_de_Terre.crapoux")
    game_loop(window)
    pygame.quit()
    quit()

main()