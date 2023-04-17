from time import sleep
from random import randint
import sys
import math
import cv2
import os
import struct

lightCoords = []
lightNum = 0
with open(r'../lightCoords.txt', 'r') as coords:
    for line in coords:
        coord = line[:-1]
        lightCoords.append([eval(coord), lightNum])
        lightNum += 1

# print(lightCoords)

xS = []
yS = []

lightNum = 0

for light in lightCoords:
    xS.append([light[0][0], lightNum])
    yS.append([light[0][1], lightNum])
    lightNum += 1

xS.sort()
yS.sort()

xOrigin = xS[0][0]
yOrigin = yS[0][0]

xDif = xS[-1][0] - xS[0][0]
yDif = yS[-1][0] - yS[0][0]

img = cv2.imread('../Images/PixelArt/biear.png')
width = img.shape[1]
height = img.shape[0]

lightNum = 0

with open("../lightOrder", "wb") as binary_file:
    for light in lightCoords:
        
        newX = math.floor((light[0][0] - xS[0][0]) * (width - 1) / xDif)
        newY = math.floor((light[0][1] - yS[0][0]) * (height - 1) / yDif)
        
        # Make sure indices are within the bounds of the image
        newX = min(max(newX, 0), width - 1)
        newY = min(max(newY, 0), height - 1)
        
        # row then column is the correct order to reference a pixel in opencv
        color = img[newY, newX]

        

        binary_file.write(lightNum.to_bytes(2, byteorder='big'))
        print(lightNum)
        # binary_file.write(lightNum.to_bytes(2, byteorder='little'))
        # # Opencv outputs colors as BGR, this is red
        binary_file.write(int(color[2]).to_bytes(1, byteorder='big'))
        print(color[2])
        # # Green
        binary_file.write(int(color[1]).to_bytes(1, byteorder='big'))
        print(color[1])

        # # Blue
        binary_file.write(int(color[0]).to_bytes(1, byteorder='big'))
        print(color[0])
        print("\n")


        lightNum += 1

