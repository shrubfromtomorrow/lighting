import board
import neopixel
from time import sleep
from random import randint
import time
pixels = neopixel.NeoPixel(board.D18, 200, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)
pixels.fill((0, 0, 0))
loops = 0
st = time.time()
while loops < 1000:
    for pixel in range(len(pixels)):
        randR = (255, 0, 0)
        randG = (255, 0, 0)
        randB = (255, 0, 0)
        pixels[pixel] = (randR, randG, randB)
    pixels.show()
    loops += 1
et = time.time()
elapsedTime = et - st
print(f"Elapsed time: {elapsedTime} seconds")

#200 lights exec time is 19.48963 sec
#100 lights exec time is 10.3855 sec
#50 lights exec time s 5.29201 sec

#Exec time is linear
