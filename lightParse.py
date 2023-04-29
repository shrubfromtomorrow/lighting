""" This file is used to parse the information provided by lightOrder on the Raspberry Pi side """

import neopixel
import board
import time
import sys

lightCount = 300

sleepTime = sys.argv[1]

loops = sys.argv[2]


pixels = neopixel.NeoPixel(board.D21, lightCount, brightness = 0.6, auto_write = False, pixel_order = neopixel.RGB)

lightOrderStr = []

totalBytes = 0

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
            totalBytes += 5
        if not chunk:
            break


for loop in range(int(loops)):
    # Loops through the number of frames, determined by the total bytes counted in previous loop, divided by 5 as each light is represented with 5 bytes, and divided by the light count.
    for frame in range(0, int((totalBytes / 5) / lightCount)):
        # Loops through all the lights in lightOrderStr in lightCount sized increments. So it would be 0,300 then 300, 400, etc..
        for light in lightOrderStr[lightCount * frame : lightCount * (frame + 1)]:
            pixels[light[0]] = light[1]
        pixels.show()
        time.sleep(float(sleepTime))
