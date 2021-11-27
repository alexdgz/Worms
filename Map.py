import numpy as np
from PIL import Image



#class Map:
from GameConfig import GameConfig


def lagrange(X): # pour tout x, je trouve son y
    ecartX = 960 // 4  # pour mettre 7 pts

    xCourant = np.array([0,ecartX,ecartX*2,ecartX*3,ecartX*4])
    yCourant = np.array([640,(640//2),650,(640//2),640])

    tabF = np.zeros(5)
    for i in range(yCourant.size):
        f = yCourant[i]
        fract = 1 # mettre à 1 car on la multiplie ensuite
        for j in range(xCourant.size):
            if(i!=j):
                fract = fract * (X - xCourant[j])/(xCourant[i]-xCourant[j])
        f = f * fract
        tabF[i] = f

    F = np.sum(tabF)

    return F

# trouvé une technique pour créer selon la dérivé ou je sais pas quoi
def mapCreate():

    img = Image.new(mode = 'RGBA', size=(640,960), color = (55,32,20,255))

    tabPix = []

    for x in range(960):
        lagr = lagrange(x)
        for y in range(640):
            if(lagr<y):
                tabPix.append((0,0,0,255))
            else:
                tabPix.append((255,255,255,0))


    img.putdata(tabPix)
    img.rotate(-90,expand=True).show()

mapCreate()


