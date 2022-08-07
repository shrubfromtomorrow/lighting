import board
import neopixel
from time import sleep
from random import randint
import sys
import colorsys
pixels = neopixel.NeoPixel(board.D18, 100, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)
pixels.fill((0, 0, 0))
pixels.show()
lightCoordsStr = []

with open(r'lightCoords.txt', 'r') as coords:
    for line in coords:
        coord = line[:-1]
        lightCoordsStr.append(coord)

lightCoords = []
for coordinate in lightCoordsStr:
    lightCoords.append(eval(coordinate))
xS = []
lightNum = 0

for light in lightCoords:
    xS.append([light[0], lightNum])
    lightNum += 1

xS.sort()

# def hsv2rgb(h,s,v):
#     return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
# def Colors(num):
#     if num <= 602*(1/10):
#         return hsv2rgb(0.0602+(0.09398*1), 1, 1)
#     elif num <= 602*(2/10):
#         return hsv2rgb(0.0602+(0.09398*2), 1, 1)
#     elif num <= 602*(3/10):
#         return hsv2rgb(0.0602+(0.09398*3), 1, 1)
#     elif num <= 602*(4/10):
#         return hsv2rgb(0.0602+(0.09398*4), 1, 1)
#     elif num <= 602*(5/10):
#         return hsv2rgb(0.0602+(0.09398*5), 1, 1)
#     elif num <= 602*(6/10):
#         return hsv2rgb(0.0602+(0.09398*6), 1, 1)
#     elif num <= 602*(7/10):
#         return hsv2rgb(0.0602+(0.09398*7), 1, 1)
#     elif num <= 602*(8/10):
#         return hsv2rgb(0.0602+(0.09398*8), 1, 1)
#     elif num <= 602*(9/10):
#         return hsv2rgb(0.0602+(0.09398*9), 1, 1)
#     elif num <= 602*(10/10):
#         return hsv2rgb(0.0602+(0.09398*10), 1, 1)


rep = 0

while rep < 100:
    color = (255, 255, 255)
    pixelIndex = int(xS[rep][1])
    pixels[pixelIndex] = color
    pixels.show()
    rep += 1
    sleep(0.01)
