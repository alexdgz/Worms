import math
import numpy as np
from PIL import Image
from GameConfig import *

class Platform:
    def func(self,va,liste_x,liste_y):
        f = 0
        for i in range(7):
            num = 1
            denum = 1
            for j in range(7):
                if i != j :
                    num *= va-liste_x[j]
                    denum *= liste_x[i]-liste_x[j]
            f += liste_y[i]*(num/denum)
        return f


def groundCreation():

    # creating a image object (new image object)
    im = Image.new(mode="RGB", size=(GameConfig.WINDOW_L,GameConfig.WINDOW_H),color=(00, 255, 00))
    imAlpha = im.convert("RGBA")

    # This method will show image in any image viewer
    imAlpha.show()
