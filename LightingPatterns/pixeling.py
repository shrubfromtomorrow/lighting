from time import sleep
from random import randint
import sys
import math

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

xS = []
yS = []

lightNum = 0

for light in lightCoords:
    xS.append([light[0][0], lightNum])
    yS.append([light[0][1], lightNum])
    lightNum += 1

xS.sort()
yS.sort()


xOrigin = xS[0][0]
yOrigin = yS[0][0]

pixelArray = []

rows, cols = (15, 10)
for i in range(rows):
    col = []
    for j in range(cols):
        col.append([])
    pixelArray.append(col)

for value in lightCoords:
    xIndex = int((value[0][0] - xOrigin)*(5/217))
    yIndex = int((value[0][1] - yOrigin)*(3/119))
    pixelArray[yIndex][xIndex].append(value[1])

lightOrder = []

reps = 5
while reps < 11:
    lightOrder.append([])
    for y in pixelArray[0:reps]:
        for x in y[0:reps]:
            for num in x[0:reps]:
                lightOrder[reps-5].append(num)
    reps += 1

with open(r'/home/orion/Code/Python/2DLighting/lightOrder.txt', 'w') as txt:
    for rep in lightOrder:
        txt.write(f"{rep}\n")
