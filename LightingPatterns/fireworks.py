import board
import neopixel
from time import sleep
from random import choice
import sys
import math
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
    while reps < 100:
        pixels[lightOrder[reps]] = Colors(distanceList[reps][0])
        pixels.show()
        reps += 1
    reps = 0
    rep += 1
