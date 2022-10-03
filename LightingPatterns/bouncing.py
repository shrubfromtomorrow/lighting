import board
import neopixel
from time import sleep
pixels = neopixel.NeoPixel(board.D18, 300, brightness = 0.3, auto_write = False, pixel_order = neopixel.GRB)

j = 0

i = 0
while True:

    if j % 2 == 0:
        while i < 299:
            if i % 1 == 0:
                pixels[i] = (0, 100, 100)
                pixels.show()
            i += 1
    else:
        while i >= 1:
            if i % 1 == 0:
                pixels[i] = (0, 0, 0)
                pixels.show()
            i -= 1
    j += 1