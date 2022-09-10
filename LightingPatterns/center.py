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

def Closest(list, point):
    valList = []
    for light in list:
        distanceSquared = (light[0][0] - point[0])**2 + (light[0][1] - point[1])**2
        valList.append([round(distanceSquared, 3), light[1]])
    valList.sort()
    return valList[0][1]


xS = [] #all y values
yS = [] #all x values

for value in lightCoords:
    xS.append(value[0][0])
    yS.append(value[0][1])

xS.sort()
yS.sort()
averageX = ((xS[0]) + (xS[-1])) / 2 #average of highest and lowest x
print(averageX)

averageY = ((yS[0]) + (yS[-1])) / 2 #average of highest and lowest y
print(averageY)

centerCoord = (averageX, averageY)

center = Closest(lightCoords, centerCoord)
print(center)

with open(r'/home/orion/Code/Python/2DLighting/lightOrder.txt', 'w') as txt:
    txt.write(f"{center}")
