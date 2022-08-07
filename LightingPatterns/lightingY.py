import board
import neopixel
from time import sleep
from random import randint
import sys
pixels = neopixel.NeoPixel(board.D18, 100, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)

lightCoordsStr = []

with open(r'lightCoords.txt', 'r') as coords:
    for line in coords:
        coord = line[:-1]
        lightCoordsStr.append(coord)

lightCoords = []
for coordinate in lightCoordsStr:
    lightCoords.append(eval(coordinate))
yS = []
lightNum = 0

for light in lightCoords:
    yS.append([light[1], lightNum])
    lightNum += 1

yS.sort()

rep = 0

while rep < 100:
    pixelIndex = int(yS[rep][1])
    pixels[pixelIndex] = (255, 255, 255)
    pixels.show()
    rep += 1
    sleep(0.01)
