import board
import neopixel
from time import sleep
from random import randint
import sys
import math

pi = math.pi

pixels = neopixel.NeoPixel(board.D18, 300, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)

lightCoordsStr = []

with open(r'lightCoords.txt', 'r') as coords:
    for line in coords:
        coord = line[:-1]
        lightCoordsStr.append(coord)

lightCoords = []
lightNum = 0
for coordinate in lightCoordsStr:
    lightCoords.append([eval(coordinate), lightNum])
    lightNum += 1


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

def Spiral(loops, points, list):
    loopRads = loops * (2*math.pi)
    pointLocsRads = []
    for point in range(1, points+1):
        pointLocsRads.append((loopRads / points)*point)
    radi = []
    for radian in pointLocsRads:
        radi.append(3*radian)
