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
        game_state.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                GameConfig.G_GAUCHE = True
                GameConfig.D_DROIT = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                GameConfig.G_GAUCHE = False
                GameConfig.D_DROIT = True



        next_move = get_next_move()
        pygame.time.delay(5)

        game_state.angle(next_move)
        game_state.variationVecteur(next_move)


        game_state.advance_state(next_move,window)
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

    if keys[pygame.K_a]:
        next_move.angle = True




    if keys[pygame.K_LCTRL]:
        next_move.angleBas = True
    if keys[pygame.K_LSHIFT]:
        next_move.angleHaut = True

    if keys[pygame.K_SPACE]:
        next_move.shoot = True

    return next_move


def main():
    pygame.init()
    GameConfig.init()
    window = pygame.display.set_mode((GameConfig.WINDOW_L, GameConfig.WINDOW_H))
    pygame.display.set_caption("CrapouxTheGame.exe")
    game_loop(window)
    pygame.quit()
    quit()

main()