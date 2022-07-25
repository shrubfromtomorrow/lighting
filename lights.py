import board
import neopixel
from time import sleep
from random import randint
import sys
import time
pixels = neopixel.NeoPixel(board.D18, 50, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)
pixels.fill((0, 0, 0))
i = int(sys.argv[1])
pixels[i] = (255, 255, 255)
pixels.show()