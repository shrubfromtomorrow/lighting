# import board
# import neopixel
from time import sleep
from random import randint
import sys
# pixels = neopixel.NeoPixel(board.D18, 100, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)

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

centerCoordSum = averageX + averageY

closestLights = {} #dictionary tying absolute value difference between center and any given light with the lightnum
closestLightsCoord = [] #list of absolute value difference between center and any given light in sorted order

lightNum = 0

for light in lightCoords:
    sum = centerCoordSum - (light[0] + light[1])
    closestLights[sum] = lightNum
    closestLightsCoord.append(sum)
    lightNum += 1

print(closestLights, end="\n\n")

closestLightsCoord = sorted(closestLightsCoord, key=abs)

lightOrder = []

for difference in closestLightsCoord:
    lightOrder.append(closestLights[difference])

print(lightOrder)


# rep = 0
#
# while rep < 100:
#     pixelIndex = int(added[rep])
#     pixels[pixelIndex] = colors[pixelIndex][1]
#     pixels.show()
#     rep += 1
#     sleep(0.01)
