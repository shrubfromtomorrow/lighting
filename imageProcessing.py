import cv2
import numpy as np
import os
import sys
import subprocess

imNum = 0

lightList = []

os.makedirs(f'Images/CircImages/{sys.argv[1]}', exist_ok=True)

for image in os.listdir(f'Images/{sys.argv[1]}'):
    f = os.path.join(f'Images/{sys.argv[1]}', image)
    if os.path.isfile(f):
        light = cv2.imread(f'Images/{sys.argv[1]}/{imNum}.jpg')

        lightRGB = np.copy(light)

        # lightGrey = np.copy(light)
        lightGrey = cv2.cvtColor(np.copy(light), cv2.COLOR_RGB2GRAY)
        lightBlur = cv2.GaussianBlur(lightGrey, (21, 21), 0)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(lightBlur)

        lightCirc = cv2.circle(lightRGB, maxLoc, 21, (0, 0, 255), 4)

        cv2.imwrite(f'Images/CircImages/{sys.argv[1]}/{imNum}Alt.jpg', lightCirc)

        lightList.append(maxLoc)

        imNum += 1

    else:
        continue
print(lightList)
with open(r'/home/orion/Code/Python/2DLighting/lightCoords.txt', 'w') as txt:
    for item in lightList:
        txt.write(f"{item}\n")
