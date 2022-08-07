import board
import neopixel
from time import sleep
from random import randint
import sys
import math
pixels = neopixel.NeoPixel(board.D18, 100, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)

lightCoordsStr = []

with open(r'lightCoords.txt', 'r') as coords:
    for line in coords:
        coord = line[:-1]
        lightCoordsStr.append(coord)

lightCoords = []
for coordinate in lightCoordsStr:
    lightCoords.append(eval(coordinate))
xS = [] #all y values
yS = [] #all x values

added = [] #sum of x and y values for all lights
lightNum = 0

for light in lightCoords:
    sum = light[0] + light[1] #adding x and y values of each light
    added.append([sum, lightNum])
    xS.append([light[0], lightNum])
    yS.append([light[1], lightNum])
    lightNum += 1

added.sort()

highXY = added[-1][1] #finding highest xy sum
lowXY = added[0][1] #finding lowest xy sum

averageX = ((xS[highXY][0]) + (xS[lowXY][0])) / 2 #average of highest and lowest x

averageY = ((yS[highXY][0]) + (yS[lowXY][0])) / 2 #average of highest and lowest y

centerCoord = (averageX, averageY)

distanceList = []
lightNum = 0

for light in lightCoords:
    xDif = abs(light[0] - centerCoord[0])
    yDif = abs(light[1] - centerCoord[1])
    distance = (xDif ** 2) + (yDif ** 2)
    distanceSqrt = round(distance ** 0.5, 4)
    distanceList.append([distanceSqrt, lightNum])
    lightNum += 1

distanceList.sort()

lightOrder = []

for distance in distanceList:
    lightOrder.append(distance[1])

pixels.fill((0, 0, 0))
pixels.show()

def Colors(num):
    if num <= 139:
        return (255, 0, 0)
    elif num <= 278:
        return (0, 255, 0)
    elif num <= 417:
        return (0, 0, 255)


reps = 0
rep = 0


while rep < 1000:
    while reps < 100:
        thisDistance = distanceList[reps][0] - (rep * 20)
        pixels[lightOrder[reps]] = Colors(thisDistance%417)
        reps += 1
    reps = 0
    sleep(0.05)
    pixels.show()
    rep += 1
