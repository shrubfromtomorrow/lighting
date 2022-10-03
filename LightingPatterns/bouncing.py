import board
import neopixel
from random import choice
from time import sleep
pixels = neopixel.NeoPixel(board.D18, 300, brightness = 0.05, auto_write = False, pixel_order = neopixel.GRB)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
teal = (0, 255, 255)
purple = (255, 0, 255)

colorList = [white, red, green, blue, yellow, teal, purple]



def bounce(fwdColor, bkwColor, fwdSkip, bkwSkip, sleepTime):
    j = 0

    i = 0
    while True:

        if j % 2 == 0:
            while i < 299:
                if i % fwdSkip == 0:
                    pixels[i] = choice(colorList)
                    sleep(sleepTime)
                if i % 5 == 0:
                    pixels.show()
                i += 1
        else:
            while i >= 1:
                if i % bkwSkip == 0:
                    pixels[i] = bkwColor
                    sleep(sleepTime)
                if i % 5 == 0:
                    pixels.show()
                i -= 1
        j += 1

bounce(white, black, 1, 1, 0)