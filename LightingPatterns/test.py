from time import sleep
from random import randint
import sys
import math
import numpy as np

lightCoordsStr = []

with open(r'../lightCoords.txt', 'r') as coords:
    for line in coords:
        coord = line[:-1]
        lightCoordsStr.append(coord)

lightCoords = []
lightNum = 0
for coordinate in lightCoordsStr:
    lightCoords.append([eval(coordinate), lightNum])
    lightNum += 1

light = 199
 
with open(r'/home/orion/Code/Python/2DLighting/lightOrder.txt', 'w') as txt:
    txt.write(f"{light}")
