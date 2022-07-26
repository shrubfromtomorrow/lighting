import board
import neopixel
from time import sleep
from random import randint
import time
pixels = neopixel.NeoPixel(board.D18, 150, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)
pixels2 = neopixel.NeoPixel(board.D21, 150, brightness = 1, auto_write = False, pixel_order = neopixel.RGB)
pixels.fill((0, 0, 0))
pixels2.fill((0, 0, 0))
loops = 0
st = time.time()
while loops < 1000:
    for pixel in range(0, 300):
        randR = randint(0, 255)
        randG = randint(0, 255)
        randB = randint(0, 255)
        if pixel in range(150, 300):
            pixels2[pixel-150] = (randR, randB, randG)
        else:
            pixels[pixel] = (randR, randB, randG)
    pixels.show()
    pixels2.show()
    
    loops += 1
et = time.time()
elapsedTime = et - st
print(f"Elapsed time: {elapsedTime} seconds")

#300 lights exec time is 28.571308 sec
#200 lights exec time is 19.48963 sec
#100 lights exec time is 10.3855 sec
#50 lights exec time s 5.29201 sec

#Exec time is linear
