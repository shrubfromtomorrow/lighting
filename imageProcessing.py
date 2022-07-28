import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# light = cv2.imread('Images/c0.png')
#
# lightRGB = np.copy(light)
# lightRGB = cv2.cvtColor(lightRGB, cv2.COLOR_RGB2BGR)
#
# lightGrey = np.copy(light)
# lightGrey = cv2.cvtColor(lightGrey, cv2.COLOR_RGB2GRAY)
# # plt.imshow(lightGrey, cmap='gray')
# # plt.show()
# print(cv2.minMaxLoc(lightGrey))
#
# maxLightX = cv2.minMaxLoc(lightGrey)[3][0]
# maxLightY = cv2.minMaxLoc(lightGrey)[3][1]
#
# l = 20
# coord1 = (maxLightX - l, maxLightY - l)
# coord2 = (maxLightX + l, maxLightY + l)
# color = (255, 0, 0)
# t = 2
#
# lightBox = np.copy(lightRGB)
# lightBox = cv2.rectangle(lightBox, coord1, coord2, color, t)
# # plt.imshow(lightBox)
# # plt.show()
#
# cv2.imwrite('Images/c0Alt.png', lightBox)

imNum = 0

lightDict = {}
lightList = []

for image in os.listdir('Images/Images100'):
    f = os.path.join('Images/Images100', image)
    if os.path.isfile(f):
        light = cv2.imread(f'Images/Images100/c{imNum}.png')

        lightRGB = np.copy(light)
        lightRGB = cv2.cvtColor(lightRGB, cv2.COLOR_RGB2BGR)

        lightGrey = np.copy(light)
        lightGrey = cv2.cvtColor(lightGrey, cv2.COLOR_RGB2GRAY)
        lightBlur = cv2.GaussianBlur(lightGrey, (21, 21), 0)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(lightBlur)

        lightCirc = cv2.circle(lightRGB, maxLoc, 21, (0, 0, 255), 4)

        cv2.imwrite(f'Images/CircIms/CircImages100/c{imNum}Alt.png', lightCirc)

        lightDict[f'Images/Images100/c{imNum}.png'] = maxLoc

        lightList.append(maxLoc)

        imNum += 1

    else:
        continue
print(lightDict)
print(lightList)
