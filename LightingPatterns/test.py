import neopixel
import board
import time
import sys
import math
import numpy as np
from random import randint

lightCount = 300

pixels = neopixel.NeoPixel(board.D21, lightCount, brightness = 0.6, auto_write = False, pixel_order = neopixel.RGB)

for i in range(20):
    for light in range(lightCount):
        print(light)
        pixels[light] = (255, 255, 255)
        pixels.show()
        time.sleep(0.1)
        pixels.fill((0, 0, 0))
        pixels.show()