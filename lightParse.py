import neopixel
import board
from time import sleep
import sys
import math
import numpy as np
from random import randint

pixels = neopixel.NeoPixel(board.D18, 300, brightness = 0.6, auto_write = False, pixel_order = neopixel.RGB)

lightOrderStr = []

with open(r'lightOrder.txt', 'r') as order:
    for line in order:
        loop = line[:-1]
        lightOrderStr.append(loop)

lightOrder = []
for loop in lightOrderStr:
    lightOrder.append(eval(loop))


############ This is code for single image pixel lighting

# for frame in lightOrder:
#     pixels.fill((0, 0, 0))
#     for pixel in frame:
#         for light in pixel[0]:
#             pixels[light] = pixel[1]
#     pixels.show()

############ This is code for pixeled lighting

# loops = 0
# while loops < 10:
#     for frame in lightOrder:
#         pixels.fill((0, 0, 0))
#         for pixel in frame:
#             for light in pixel[0]:
#                 pixels[light] = pixel[1]
#         sleep(.03)
#         pixels.show()
#     loops += 1

############ This is code for a lighting pattern

loops = 0
while loops < 5:
    turns = 0
    while turns < len(lightOrder):
        pixels.fill((0, 0, 0))
        for light in lightOrder[turns]:
            pixels[light] = (255, 255, 255)
        pixels.show()
        sleep(0.1)
        turns += 1
    loops += 1
