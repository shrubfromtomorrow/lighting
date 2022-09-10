import board
import neopixel
from time import sleep
from random import randint
import sys
import math
pixels = neopixel.NeoPixel(board.D18, 300, brightness = 0.1, auto_write = False, pixel_order = neopixel.RGB)

pixels.fill((255, 255, 255))
pixels.show()
