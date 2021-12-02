# import des modules et des autres fichiers
from GameState import *
from Move import *
from GameConfig import *
import pygame

def game_loop(window):
    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
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

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                game_state.Shoot.rect = pygame.Rect(
                                game_state.worm.rect.left,
                                game_state.worm.rect.top,
                                GameConfig.projectile_W,
                                GameConfig.projectile_H)


        next_move = get_next_move()
        pygame.time.delay(7)

        game_state.angle(next_move)
        game_state.variationVecteur(next_move)

        if game_state.worm2.hp == 0:
            textsurface = myfont.render('Victoire du Crapoux numéro 1', False, (0, 0, 0))
            window.blit(textsurface,(0,0))
            pygame.time.delay(100)
            quitting = True
        if game_state.worm.hp == 0:
            textsurface = myfont.render('Victoire du Crapoux numéro 2', False, (0, 0, 0))
            window.blit(textsurface, (0, 0))
            pygame.time.delay(100   )
            quitting = True

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
    window = pygame.display.set_mode((GameConfig.WINDOW_L, GameConfig.WINDOW_H))
    GameConfig.init()
    pygame.display.set_caption("CrapouxTheGame.exe")
    game_loop(window)
    pygame.quit()
    quit()

main()