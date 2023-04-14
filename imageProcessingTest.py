import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import subprocess

imNum = 0

lightDict = {}
lightList = []

os.mkdir(f'Images/CircImages/{sys.argv[1]}')

for image in os.listdir(f'Images/{sys.argv[1]}'):
    f = os.path.join(f'Images/{sys.argv[1]}', image)
    if os.path.isfile(f):
        light = cv2.imread(f'Images/{sys.argv[1]}/c{imNum}.png')

        lightRGB = np.copy(light)
        lightRGB = cv2.cvtColor(lightRGB, cv2.COLOR_RGB2BGR)

        lightGrey = np.copy(light)
        lightGrey = cv2.cvtColor(lightGrey, cv2.COLOR_RGB2GRAY)
        lightBlur = cv2.GaussianBlur(lightGrey, (21, 21), 0)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(lightBlur)

        lightCirc = cv2.circle(lightRGB, maxLoc, 21, (0, 0, 255), 4)

        cv2.imwrite(f'Images/CircImages/{sys.argv[1]}/c{imNum}Alt.jpg', lightCirc)

        lightDict[f'Images/{sys.argv[1]}/c{imNum}.jpg'] = maxLoc

        lightList.append(maxLoc)

        imNum += 1

    else:
        continue
with open(r'./lightCoords.txt', 'w') as txt:
    for item in lightList:
        txt.write(f"{item}\n")

# scp = ["scp", f"/home/orion/Code/Python/2DLighting/lightCoords.txt", "pi@192.168.10.223:"]
# subprocess.run(scp)
