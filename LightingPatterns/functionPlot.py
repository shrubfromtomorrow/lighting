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
    return valList[0]


xS = [] #all y values
yS = [] #all x values

added = [] #sum of x and y values for all lights
lightNum = 0

for light in lightCoords:
    sum = light[0][0] + light[0][1] #adding x and y values of each light
    added.append([sum, lightNum])
    xS.append([light[0][0], lightNum])
    yS.append([light[0][1], lightNum])
    lightNum += 1

added.sort()

highXY = added[-1][1] #finding highest xy sum
lowXY = added[0][1] #finding lowest xy sum

averageX = ((xS[highXY][0]) + (xS[lowXY][0])) / 2 #average of highest and lowest x

averageY = ((yS[highXY][0]) + (yS[lowXY][0])) / 2 #average of highest and lowest y

centerCoord = (averageX, averageY)
newCoords = []
lightNum = 0

for light in lightCoords:
    xDif = light[0][0] - centerCoord[0]
    yDif = light[0][1] - centerCoord[1]
    newCoords.append([[xDif, -1 * yDif], lightNum])
    lightNum += 1

linearCoords = []

for light in range(-450, 600):
    linearCoords.append([light, 200 * (math.sin((1/80) * light))])


lightOrderDups = [[]]

for point in linearCoords:
    lightOrderDups[0].append(Closest(newCoords, point)[1])
lightOrder = [*set(lightOrderDups[0])]
with open(r'/home/orion/Code/Python/2DLighting/lightOrder.txt', 'w') as txt:
    for turn in lightOrder:
        # turn = [*set(turn)]
        txt.write(f"{turn}\n")