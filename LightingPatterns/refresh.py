import board
import neopixel
from time import sleep
from random import randint
import sys
import math
pixels2 = neopixel.NeoPixel(board.D12, 150, brightness = 0.2, auto_write = False, pixel_order = neopixel.RGB)

pixels2.fill((255, 255, 255))
pixels2.show()
