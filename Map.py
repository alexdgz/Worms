import random
import numpy as np
from PIL import Image

class Map:

    def __init__(self):
        self.yCourant =  np.array([random.randint(540,600), random.randint(400,450), random.randint(600,700), random.randint(350,400), random.randint(540,640)])



    def lagrange(self, X): # pour tout x, je trouve son y
        ecartX = 960 // 4  # pour mettre 5 pts

        xCourant = np.array([20,ecartX,ecartX*2,ecartX*3,ecartX*4-20])
        
        tabF = np.zeros(len(xCourant))

        for i in range(self.yCourant.size):
            f = self.yCourant[i]
            fract = 1 # mettre à 1 car on la multiplie ensuite
            for j in range(xCourant.size):
                if(i!=j):
                    fract = fract * (X - xCourant[j])/(xCourant[i]-xCourant[j])
            f = f * fract
            tabF[i] = f

        F = np.sum(tabF)

        return F

    # trouvé une technique pour créer selon la dérivé ou je sais pas quoi
    def mapCreate(self):

        courbe = Image.new(mode = 'RGBA', size=(640,960), color = (55,32,20,255))

        tabPix = []


        for x in range(960):
            lagr = self.lagrange(x)
            for y in range(640):
                if(lagr<y):
                    tabPix.append((0,0,0,255))
                else:
                    tabPix.append((255,255,255,0))



        courbe.putdata(tabPix)

        imgTerrainFinal = Image.new(mode = 'RGBA', size=(960,640), color = (55,32,20,0))
        dirt = Image.open("ressources/dirt.png")
        courbe = courbe.rotate(-90,expand=True)

        imgTerrainFinal.paste(dirt, (0,0), courbe)
        imgTerrainFinal.save("ressources/terrain_asset.png", format='png')

        #imgBlancFond = Image.new(mode = 'RGBA', size=(960,640), color = (255,255,255,255))
        #imgBlancFond.save("ressources/background.png", format='png')





