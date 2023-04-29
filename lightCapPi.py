""" This is the file that is on the Raspberry Pi that is called by imageCapture.py to light an individual light up """

import board
import neopixel
from time import sleep
from random import randint
import sys
light = int(sys.argv[1])
print(light)
pixels = neopixel.NeoPixel(board.D21, 300, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)
pixels.fill((0, 0, 0))
pixels.show()
pixels[light] = (255, 255, 255)
pixels.show()
print("Ready for picture")
