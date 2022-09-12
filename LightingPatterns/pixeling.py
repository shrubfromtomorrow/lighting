from time import sleep
from random import randint
import sys
import math
import cv2
import os

lightCoordsStr = []

with open(r'../lightCoords.txt', 'r') as coords:
    for line in coords:
        coord = line[:-1]
        lightCoordsStr.append(coord)

lightCoords = []
lightNum = 0
for coordinate in lightCoordsStr:
    lightCoords.append([eval(coordinate), lightNum])
    lightNum += 1

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

pixelArray = []
def DetArray(x, y):
    rows, cols = (y, x)
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append([])
        pixelArray.append(col)
    for value in lightCoords:
        xIndex = int((value[0][0] - xOrigin)*((x-0.00001)/xDif))
        yIndex = int((value[0][1] - yOrigin)*((y-0.00001)/yDif))
        pixelArray[yIndex][xIndex].append(value[1])



# def rgb_to_hex(rgb):
#     return '#%02x%02x%02x' % rgb



# file = sys.argv[1]

fullPixelArray = []

fileOrder = os.listdir("/home/orion/Pictures/PixelArt/2bLit/")
print(fileOrder)
#fileOrder.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

for file in fileOrder:
    print(file)
    im = cv2.imread(f'/home/orion/Pictures/PixelArt/2bLit/{file}')
    imRGB = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)


    def Fill(index, color):
        lightOrder = [pixelArray[index[0]][index[1]], color]
        return lightOrder

    DetArray(len(imRGB[0]), len(imRGB))

    pixelAssign = []

    rowNum = 0
    for row in imRGB:
        colNum = 0
        for column in row:
            color = (column[0], column[1], column[2])
            # print(rgb_to_hex(color))
            pixelAssign.append(Fill([rowNum, colNum], color))
            colNum += 1
        # print("\n")
        rowNum += 1
    fullPixelArray.append(pixelAssign)
# print(fullPixelArray)


with open(r'/home/orion/Code/Python/2DLighting/lightOrder.txt', 'w') as txt:
    for rep in fullPixelArray:
        txt.write(f"{rep}\n")
