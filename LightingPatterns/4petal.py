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

xS.sort()
yS.sort()

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

def Flower(petalNum, pointsNum, rotRad):
    pointsLocsRads = []
    for num in range(1, pointsNum):
        pointsLocsRads.append(((2*math.pi)/pointsNum)*num)
    pointsLocsRads.sort()
    radi = []
    for radian in pointsLocsRads:
        radi.append(abs(400*(math.cos(2*radian))))
    pointsLocsRadsAlt = []
    for point in pointsLocsRads:
        pointsLocsRadsAlt.append(point + rotRad)
    pointsLocs = []
    pointNum = 0
    for radius in radi:
        x = round(math.cos(pointsLocsRadsAlt[pointNum]) * radius, 3)
        y = round(math.sin(pointsLocsRadsAlt[pointNum]) * radius, 3)
        pointsLocs.append([x, y])
        pointNum += 1
    return pointsLocs

lightOrder = []
loops = 0
while loops < 10:
    lightOrderCoords = []
    rotRad = math.pi/2
    lightOrder.append([])
    lightOrderCoords = Flower(4, 75, rotRad*loops)
    for light in lightOrderCoords:
        lightOrder[loops].append(Closest(newCoords, light)[1])
    loops += 1

with open(r'/home/orion/Code/Python/2DLighting/lightOrder.txt', 'w') as txt:
    for turn in lightOrder:
        # turn = [*set(turn)]
        txt.write(f"{turn}\n")
