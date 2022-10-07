import neopixel
import board
from time import sleep
import sys
import math
import numpy as np
from random import randint

pixels = neopixel.NeoPixel(board.D18, 300, brightness = 0.6, auto_write = False, pixel_order = neopixel.RGB)

lightOrderStr = []

with open(r'lightOrder.txt', 'r') as order:
   for line in order:
       loop = line[:-1]
       lightOrderStr.append(loop)

lightOrder = []
for loop in lightOrderStr:
   lightOrder.append(eval(loop))


############ This is code for single image pixel lighting
# pixels1 = neopixel.NeoPixel(board.D18, 150, brightness = 0.6, auto_write = False, pixel_order = neopixel.RGB) 
# pixels2 = neopixel.NeoPixel(board.D21, 150, brightness = 0.6, auto_write = False, pixel_order = neopixel.RGB)
# for frame in lightOrder:
#     pixels1.fill((0, 0, 0))
#     pixels2.fill((0, 0, 0))
#     for pixel in frame:
#         for light in pixel[0]:
#             if light in range(150, 300):
#                 pixels2[light-150] = pixel[1]
#             else:
#                 pixels1[light] = pixel[1]
#     pixels1.show()
#     pixels2.show()

############ This is code for pixeled lighting

# loops = 0
# while loops < 10:
#    for frame in lightOrder:
#        pixels.fill((0, 0, 0))
#        for pixel in frame:
#             pixels[pixel] = (255, 255, 255)
#        pixels.show()
#    loops += 1

############ This is code for a lighting pattern

# pixels1 = neopixel.NeoPixel(board.D18, 150, brightness = 0.6, auto_write = False, pixel_order = neopixel.RGB) 
# pixels2 = neopixel.NeoPixel(board.D21, 150, brightness = 0.6, auto_write = False, pixel_order = neopixel.RGB)
# pixels1.fill((0, 0, 0))
# pixels2.fill((0, 0, 0))
# for pixel in lightOrder:
#     print(pixel)
#     if pixel in range(150, 300):
#         pixels2[pixel-150] = (255, 255, 255)
#     else:
#         pixels1[pixel] = (255, 255, 255)
# pixels1.show()
# pixels2.show()


############ This is code for separating the lights into sections of 150 

# pixels1 = neopixel.NeoPixel(board.D18, 150, brightness = 0.6, auto_write = False, pixel_order = neopixel.RGB) 
# pixels2 = neopixel.NeoPixel(board.D21, 150, brightness = 0.6, auto_write = False, pixel_order = neopixel.RGB)
# loops = 0
# while loops < 50:
#    for frame in lightOrder:
#        pixels1.fill((0, 0, 0))
#        pixels2.fill((0, 0, 0))
#        for pixel in frame:
#            for light in pixel[0]:
#                if light in range(150, 300):
#                    pixels2[light-150] = pixel[1]
#                else:
#                    pixels1[light] = pixel[1]
#        pixels1.show()
#        pixels2.show()
#    loops += 1

########### Single lane animation

# pixels1 = neopixel.NeoPixel(board.D18, 300, brightness = 0.6, auto_write = False, pixel_order = neopixel.RGB) 
# loops = 0
# while loops < 10:
#     for frame in lightOrder:
#         pixels1.fill((0, 0, 0))
#         for pixel in frame:
#            for light in pixel[0]:
#                 pixels1[light] = pixel[1]
#         pixels1.show()
#         sleep(1)
#     loops += 1


# pixels1 = neopixel.NeoPixel(board.D18, 300, brightness = 0.6, auto_write = False, pixel_order = neopixel.RGB) 
# for frame in lightOrder:
#     pixels1.fill((0, 0, 0))
#     for pixel in frame:
#         for light in pixel[0]:
#             pixels1[light] = pixel[1]
#     pixels1.show()
