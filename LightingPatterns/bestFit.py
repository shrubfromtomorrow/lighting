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

###For finding ranges of xs and ys range currently is 464-896x, 58-648y
# highX = []
# highY = []
# for light in lightCoords:
#     highX.append(light[0][0])
#     highY.append(light[0][1])
# highX.sort()
# highY.sort()
# range = f"{str(highX[0])}x - {str(highX[-1])}x, {str(highY[0])}y - {str(highY[-1])}y"
# print(range)

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

distanceList = []
newCoords = []
lightNum = 0

for light in lightCoords:
    xDif = light[0][0] - centerCoord[0]
    yDif = light[0][1] - centerCoord[1]
    newCoords.append([[xDif, -1 * yDif], lightNum])
    distance = (xDif ** 2) + (yDif ** 2)
    distanceSqrt = round(distance ** 0.5, 4)
    distanceList.append([distanceSqrt, lightNum])
    lightNum += 1
distanceList.sort()

def Closest(list, point):
    valList = []
    for light in list:
        distanceSquared = (light[0][0] - point[0])**2 + (light[0][1] - point[1])**2
        valList.append([distanceSquared, light[1]])
    valList.sort()
    return valList[0]


def PointsInCircum(r, n=1000):
    return [(round(math.cos(2*pi/n*x)*r, 4) , round(math.sin(2*pi/n*x)*r, 4)) for x in range(0,n+1)]

points = [PointsInCircum(120)]
lightsDup = []
for point in points[0]:
    lightsDup.append(Closest(newCoords, point)[1])
lights = [*set(lightsDup)]
print(lights)
pixels.fill((0, 0, 0))
pixels.show()
for light in lights:
    pixels[light] = (255, 255, 255)
pixels.show()
