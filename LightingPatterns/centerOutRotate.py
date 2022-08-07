import numpy as np
import math
import board
import neopixel
from time import sleep

pixels = neopixel.NeoPixel(board.D18, 100, brightness = 0.5, auto_write = False, pixel_order = neopixel.RGB)


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
newCoords = []
lightNum = 0

for light in lightCoords:
    xDif = light[0] - centerCoord[0]
    yDif = light[1] - centerCoord[1]
    newCoords.append([[xDif, -1 * yDif], lightNum])
    distance = (xDif ** 2) + (yDif ** 2)
    distanceSqrt = round(distance ** 0.5, 4)
    distanceList.append([distanceSqrt, lightNum])
    lightNum += 1
distanceList.sort()

##############################################

lightNum = 0
loops = 0

def Hex(num):
    num = str(num)
    splitStr = num.split(" ")
    r = int(splitStr[0], 16)
    g = int(splitStr[1], 16)
    b = int(splitStr[2], 16)
    dec = (r, g, b)
    return dec

while loops < 100:
    for light in newCoords:
        startingVector = np.array([[light[0][0]], [light[0][1]]])
        angle = math.pi/12
        rotationMatrix = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        resUnrounded = np.matmul(rotationMatrix, startingVector)
        res = np.round(resUnrounded, decimals=2)
        newCoords[lightNum] = [[res[0][0], res[1][0]], lightNum]

        radians = math.atan(newCoords[lightNum][0][1] / newCoords[lightNum][0][0])


        if newCoords[lightNum][0][0] > 0 and newCoords[lightNum][0][1] > 0:
            radians = round(radians, 4)
        elif newCoords[lightNum][0][0] < 0 and newCoords[lightNum][0][1] > 0:
            radians += math.pi
            radians = round(radians, 4)
        elif newCoords[lightNum][0][0] < 0 and newCoords[lightNum][0][1] < 0:
            radians += math.pi
            radians = round(radians, 4)
        elif newCoords[lightNum][0][0] > 0 and newCoords[lightNum][0][1] < 0:
            radians += math.pi * 2
            radians = round(radians, 4)

        if 0 < radians <= (2*math.pi) / 7:
            pixels[lightNum] = Hex("ff 00 00")
        elif (2*math.pi) / 7 < radians <= (4*math.pi) / 7:
            pixels[lightNum] = Hex("ff a5 00")
        elif (4*math.pi) / 7 < radians <= (6*math.pi) / 7:
            pixels[lightNum] = Hex("ff ff 00")
        elif (6*math.pi) / 7 < radians <= (8*math.pi) / 7:
            pixels[lightNum] = Hex("00 80 00")
        elif (8*math.pi) / 7 < radians <= (10*math.pi) / 7:
            pixels[lightNum] = Hex("00 00 ff")
        elif (10*math.pi) / 7 < radians <= (12*math.pi) / 7:
            pixels[lightNum] = Hex("4b 00 82")
        elif (12*math.pi) / 7 < radians <= (14*math.pi) / 7:
            pixels[lightNum] = Hex("ee 82 ee")
        lightNum += 1

    pixels.show()
    sleep(0.01)
    lightNum = 0
    loops += 1
