import board
import neopixel
from time import sleep
pixels18 = neopixel.NeoPixel(board.D18, 300, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)
pixels21 = neopixel.NeoPixel(board.D21, 300, brightness = 1, auto_write = False, pixel_order = neopixel.GRB)


k = 0

while True:
    j = 0

    while j < 10:
        i = 0
        while i < 300:
            if i % 10 == j:
                pixels18[i] = (255, 255, 255)
                pixels21[i] = (255, 0, 0)
                i += 1
            else:
                pixels18[i] = (0, 0, 0)
                pixels21[i] = (0, 0, 0)
                i += 1
        pixels18.show()
        pixels21.show()
        sleep(0.1)
        j += 1
    k += 1
