import random
import numpy as np
from PIL import Image

class Map:
    # définition des images voulues avec le calcul de lagrange
    def __init__(self):
        self.yCourant =  np.array([random.randint(540,600), random.randint(400,450), random.randint(600,700), random.randint(350,400), random.randint(540,640)])


    # fonction qui calcule lagrange
    def lagrange(self, X): # pour tout x, je trouve son y
        ecartX = 960 // 4  # pour placer 5 points

        xCourant = np.array([20,ecartX,ecartX*2,ecartX*3,ecartX*4-20]) #pour séparer l'écran en 5
        
        tabF = np.zeros(len(xCourant))

        for i in range(self.yCourant.size):
            f = self.yCourant[i]
            fract = 1 # mettre à 1 car on la multiplie ensuite
            for j in range(xCourant.size):
                if(i!=j):
                    fract = fract * (X - xCourant[j])/(xCourant[i]-xCourant[j]) # calcule de chaque fonctions ou la fonction, en x, passe par 1 et 0 pour tout les autres points
            f = f * fract # on multiplie le résultat par le y courant.
            tabF[i] = f #ajout de la fonction que l'on vient de calculer dans un tableau

        F = np.sum(tabF) #on effectue la somme des fonction que l'on a calculer

        return F

    # Méthode pour créer une image selon le polynôme calculé
    def mapCreate(self):
        courbe = Image.new(mode = 'RGBA', size=(640,960), color = (55,32,20,255)) # création de l'image
        tabPix = []
        for x in range(960): # parcours de la largeur de la fenêtre
            lagr = self.lagrange(x)
            for y in range(640): # parcours de la hauteur de la fenêtre
                if(lagr<y):
                    tabPix.append((0,0,0,255)) #couleur noir
                else:
                    tabPix.append((255,255,255,0)) #couleur blanche



        courbe.putdata(tabPix) #ajout des pixels sur l'image

        imgTerrainFinal = Image.new(mode = 'RGBA', size=(960,640), color = (55,32,20,0))
        dirt = Image.open("ressources/dirt.png")
        courbe = courbe.rotate(-90,expand=True)

        imgTerrainFinal.paste(dirt, (0,0), courbe) # on superpose le terrain sur le fond
        imgTerrainFinal.save("ressources/terrain_asset.png", format='png') # on save l'image