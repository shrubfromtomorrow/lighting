import numpy as np
import math
import board
import neopixel
from time import sleep

pixels = neopixel.NeoPixel(board.D18, 100, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)


lightCoords = [(116, 437), (129, 483), (134, 522),
(88, 540), (133, 575), (96, 639), (134, 639),
(126, 672), (172, 653), (172, 656), (246, 622),
(224, 563), (223, 565), (195, 533), (234, 498),
(265, 437), (210, 392), (207, 390), (244, 359),
(264, 350), (255, 276), (254, 297), (262, 204),
(271, 206), (243, 184), (276, 132), (276, 114),
(259, 92), (285, 76), (253, 56), (253, 19),
(359, 77), (276, 46), (309, 100), (284, 97),
(288, 127), (314, 131), (264, 198), (265, 194),
(274, 244), (278, 276), (317, 324), (364, 313),
(277, 378), (305, 321), (270, 436), (270, 429),
 (313, 477), (311, 527), (263, 505), (263, 657),
 (268, 685), (321, 712), (271, 718), (389, 713),
 (418, 693), (374, 656), (375, 636), (378, 634),
 (394, 620), (371, 577), (414, 540), (417, 508),
 (409, 513), (390, 472), (408, 450), (395, 413),
 (391, 367), (396, 388), (429, 413), (428, 463),
 (411, 469), (424, 525), (428, 543), (431, 573),
 (403, 602), (409, 621), (445, 661), (433, 677),
 (480, 683), (515, 676), (536, 648), (537, 639),
 (547, 575), (532, 572), (555, 523), (542, 503),
 (537, 480), (538, 456), (570, 439), (549, 409),
 (555, 414), (594, 424), (595, 447), (557, 464),
 (596, 499), (602, 501), (589, 550), (589, 555),
 (591, 582)]

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

        if 0 < radians <= math.pi / 2:
            pixels[lightNum] = (255, 0, 0)
        elif math.pi / 2 < radians <= math.pi:
            pixels[lightNum] = (0, 255, 0)
        elif math.pi < radians <= math.pi * 1.5:
            pixels[lightNum] = (0, 0, 255)
        elif math.pi * 1.5 < radians <= math.pi * 2:
            pixels[lightNum] = (255, 0, 255)
        lightNum += 1

    pixels.show()
    sleep(0.05)
    lightNum = 0
    loops += 1
