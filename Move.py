import pygame

class Move:
    def __init__(self):
        self.left = False
        self.right = False
        self.jump = False
        self.shoot = False

        #self.tireDroit = False
        #self.tireGauche = False

        self.angleHaut = False #shift
        self.angleBas = False #ctrl

        self.angle = False

        self.puissance = False