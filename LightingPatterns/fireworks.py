import board
import neopixel
from time import sleep
from random import choice
import sys
import math
pixels = neopixel.NeoPixel(board.D18, 200, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)

lightCoordsStr = []

with open(r'lightCoords.txt', 'r') as coords:
    for line in coords:
        coord = line[:-1]
        lightCoordsStr.append(coord)

lightCoords = []
for coordinate in lightCoordsStr:
    lightCoords.append(eval(coordinate))

rep = 0
reps = 0

def Colors(num):
    if num <= 0:
        return (255, 255, 255)
    elif num <= 100:
        return (255, 0, 0)
    elif num <= 200:
        return (255, 0, 0)
    elif num <= 300:
        return (0, 255, 0)
    elif num <= 400:
        return (0, 255, 255)
    elif num <= 500:
        return (0, 0, 255)
    elif num <= 600:
        return (255, 0, 255)
    elif num > 600:
        return (100, 255, 100)


while rep < 10:
    pixels.fill((0, 0, 0))
    pixels.show()
    distanceList = []
    lightNum = 0
    centerCoord = choice(lightCoords)
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
    while reps < 200:
        pixels[lightOrder[reps]] = Colors(distanceList[reps][0])
        pixels.show()
        reps += 1
    reps = 0
    rep += 1
