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


turns = 0
while turns < len(lightOrder):
    pixels.fill((0, 0, 0))
    for light in lightOrder[turns]:
        pixels[light] = (255, 255, 255)
    pixels.show()
    sleep(0.3)
    turns += 1
