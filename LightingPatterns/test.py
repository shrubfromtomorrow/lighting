import board
import neopixel
from time import sleep
pixels = neopixel.NeoPixel(board.D18, 100, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)
pixels.fill((0, 0, 0))
pixels.show()
pixels[13] = (255, 255, 255)
pixels.show()
