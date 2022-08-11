import board
import neopixel
from time import sleep
from random import randint
import sys
pixels = neopixel.NeoPixel(board.D18, 300, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)

lightCoordsStr = []

with open(r'lightCoords.txt', 'r') as coords:
    for line in coords:
        coord = line[:-1]
        lightCoordsStr.append(coord)

lightCoords = []
for coordinate in lightCoordsStr:
    lightCoords.append(eval(coordinate))
added = []
lightNum = 0

for light in lightCoords:
    sum = light[0] + light[1]
    added.append([sum, lightNum])
    lightNum += 1

added.sort()

# def Color(num):
#     if num <= 238:
#         return (255, 255, 255)
#     elif num <= 238 + 238:
#         return (255, 0, 0)
#     elif num <= 238 + (238 * 2):
#         return (0, 255, 0)
#     elif num <= 238 + (238 * 3):
#         return (0, 0, 255)
#     elif num <= 239 + (238 * 4):
#         return (0, 255, 255)
# colors = []
#
# for light in added:
#     colors.append([light[1], Color(light[0])])
#
# print(added, end="\n\n")
# print(colors, end="\n\n")

rep = 0

while rep < 300:
    pixelIndex = int(added[rep][1])
    pixels[pixelIndex] = (255, 255, 255)
    pixels.show()
    rep += 1
    sleep(0.01)
