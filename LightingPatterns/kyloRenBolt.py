import board
import neopixel
from random import choice
from random import randint
from time import sleep
pixels = neopixel.NeoPixel(board.D18, 300, brightness = 1, auto_write = False, pixel_order = neopixel.GRB)



j = 0
i = 0
while True:
    if j % 2 == 0:
        while i < 299:
            if i % 1 == 0:
                if i == 150:
                    h = 0
                    while h < 50:
                        if h % 2 == 0:
                            pixels.fill((0, 0, 0))
                            for x in range(1, 11):
                                print(x)
                                pixels[i-x] = (255, 255-(5*h), 255-(5*h))
                            h += 1
                            pixels.show()
                            sleep(0.01)
                        else:
                            pixels.fill((0, 0, 0))
                            for x in range(0, 10):
                                pixels[i-x] = (255, 255-(5*h), 255-(5*h))
                            h += 1
                            pixels.show()
                            sleep(0.01)
                else:
                    pixels.fill((0, 0, 0))
                    for x in range(0, 10):
                        pixels[i-x] = (255, 255, 255)
            if i % 2 == 0:
                pixels.show()
            i += 1
    else:
        while i >= 1:
            if i == 150:
                h = 0
                while h < 50:
                    if h % 2 == 0:
                        pixels.fill((0, 0, 0))
                        for x in range(1, 11):
                            print(x)
                            pixels[i-x] = (255, 255-(5*h), 255-(5*h))
                        h += 1
                        pixels.show()
                        sleep(0.01)
                    else:
                        pixels.fill((0, 0, 0))
                        for x in range(0, 10):
                            pixels[i-x] = (255, 255-(5*h), 255-(5*h))
                        h += 1
                        pixels.show()
                        sleep(0.01)
            else:
                pixels.fill((0, 0, 0))
                for x in range(0, 10):
                    pixels[i-x] = (255, 255, 255)
            if i % 2 == 0:
                pixels.show()
            i -= 1
    j += 1