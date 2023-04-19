import math
import cv2
import os
import time

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

print(xDif, yDif)

def outputLightOrder():
    print(fileOrder)

    st = time.time()

    with open("../lightOrder", "wb") as binary_file:
        for file in fileOrder:
            lightNum = 0
            img = cv2.imread(os.path.join("../Images/PixelArt/frames/", file))
            width = img.shape[1]
            height = img.shape[0]
            for light in lightCoords:
                
                # This is a calculation of the ratio of the light x and y to the difference between max x and max y. Applying this same ratio to pixel value on image width or height:

                # lightX | ?
                # ------ | ------
                # xDif   | widthOfIm


                newX = math.floor((light[0][0] - xS[0][0]) * (width - 1) / xDif)
                newY = math.floor((light[0][1] - yS[0][0]) * (height - 1) / yDif)
                
                # # Make sure indices are within the bounds of the image
                # newX = min(max(newX, 0), width - 1)
                # newY = min(max(newY, 0), height - 1)
                
                # row then column is the correct order to reference a pixel in opencv
                color = img[newY, newX]

                
                # Lightnumber is under 16bits but over 8bits and as such requires two bytes
                binary_file.write(lightNum.to_bytes(2, byteorder='big'))
                # Opencv outputs colors as BGR, this is red
                binary_file.write(int(color[2]).to_bytes(1, byteorder='big'))
                # Green
                binary_file.write(int(color[1]).to_bytes(1, byteorder='big'))
                # Blue
                binary_file.write(int(color[0]).to_bytes(1, byteorder='big'))


                lightNum += 1


fileOrder = os.listdir("../Images/PixelArt/frames/")

try:
    fileOrder.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    outputLightOrder()
except ValueError:
    print("File(s) contain no numbers, proceeding in order")

    outputLightOrder()

    et = time.time()

    elapsed = et - st
    print(elapsed)