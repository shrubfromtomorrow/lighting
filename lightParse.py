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

pixels.fill((0, 0, 0))
for pixel in lightOrder:
    for light in pixel[0]:
        pixels[light] = pixel[1]
pixels.show()
