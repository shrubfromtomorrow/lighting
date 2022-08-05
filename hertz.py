import board
import neopixel
from time import sleep
from random import randint
import time
pixels = neopixel.NeoPixel(board.D18, 50, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)
pixels.fill((0, 0, 0))
loops = 0
st = time.time()
while loops < 1000:
    for pixel in range(len(pixels)):
        randR = randint(0,255)
        randG = randint(0,255)
        randB = randint(0,255)
        pixels[pixel] = (randR, randG, randB)
    pixels.show()
    loops += 1
et = time.time()
elapsedTime = et - st
print(f"Elapsed time: {elapsedTime} seconds")

#100 lights exec time is 10.3855 sec
#50 lights exec time s 5.29201 sec
