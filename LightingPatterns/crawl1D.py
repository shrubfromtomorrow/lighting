import board
import neopixel
from time import sleep
pixels = neopixel.NeoPixel(board.D18, 300, brightness = 1, auto_write = False, pixel_order = neopixel.GRB)


k = 0

while True:
    j = 0

    while j < 10:
        i = 0
        while i < 300:
            if i % 10 == j:
                pixels[i] = (255, 255, 255)
                i += 1
            else:
                pixels[i] = (30, 30, 30)
                i += 1
        pixels.show()
        sleep(0.1)
        j += 1
    k += 1
