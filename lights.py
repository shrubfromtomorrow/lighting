import board
import neopixel
from time import sleep
from random import randint
import sys
import time
pixels = neopixel.NeoPixel(board.D18, 50, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)
pixels.fill((0, 0, 0))
pixels.show()
lightList = sys.argv[1:]

reps = 0

lightListRev = lightList
# lightListRev.reverse()

while reps < 50:
    pixelIndex = int(lightListRev[reps])
    pixels[pixelIndex] = (255, 255, 255)
    pixels.show()
    reps += 1
    sleep(0.05)
