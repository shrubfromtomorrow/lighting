# This file controls LEDs and lights them up in increasing x-coordinate order

import board
import neopixel
from time import sleep
from random import randint
import sys

# Sets the delay between each light and the number of loops to the first and second argument inputted from running the program
delay = sys.argv[1]
loops = sys.argv[2]

lightCoords = []
lightNum = 0
# Open lightCoords.txt and reads the coordinates of each light and its light number into a list of length 2
with open(r'lightCoords.txt', 'r') as coords:
    for line in coords:
        coord = line[:-1]
        lightCoords.append([eval(coord), lightNum])
        lightNum += 1

# Create separate list for x coordinates and their corresponding light number and sorts the list based on x value
xS = []
lightNum = 0
for light in lightCoords:
    xS.append([light[0], lightNum])
    lightNum += 1

xS.sort()


color = (255, 255, 255)

loop = 0

# Loops through all of the lights and turns each light to white in x-coordinate order. Loops as many times as declared at the beginning of this file
while loop < loops:
    light = 0
    while light < 300:
        pixelIndex = int(xS[rep][1])
        pixels[pixelIndex] = color
        pixels.show()
        light += 1
        sleep(delay)
    loop += 1
