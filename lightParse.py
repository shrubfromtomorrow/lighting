import neopixel
import board
import time
import sys
import math
import numpy as np
from random import randint

lightCount = 300

pixels = neopixel.NeoPixel(board.D21, lightCount, brightness = 0.6, auto_write = False, pixel_order = neopixel.RGB)

lightOrderStr = []

with open('lightOrder', 'rb') as order:
    while True:
        bytesRead = 0
        while bytesRead < lightCount * 5:
            # Read the file in chunks of 5 bytes
            chunk = order.read(5)
            # If the chunk is empty, we have reached the end of the file (end of all frames)
            if not chunk:
                break
            lightNum = int.from_bytes(chunk[:2], byteorder="big")
            color = tuple(chunk[2:])
            lightOrderStr.append([lightNum, color])
            bytesRead += 5
        if not chunk:
            break

        # TEST LIGHTING WHILE PARSING OR PARSING THEN LIGHTING AFTER USING LIGHTORDERSTR


for i in range(300):
    for light in lightOrderStr:
        if light[0] == 299:
            pixels.show()
            # time.sleep(0.1)
        pixels[light[0]] = light[1]

# pixels.show()