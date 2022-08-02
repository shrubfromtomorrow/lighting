import numpy as np
import math
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

lightCoords = [(116, 437), (129, 483), (134, 522),
(88, 540), (133, 575), (96, 639), (134, 639),
(126, 672), (172, 653), (172, 656), (246, 622),
(224, 563), (223, 565), (195, 533), (234, 498),
(265, 437), (210, 392), (207, 390), (244, 359),
(264, 350), (255, 276), (254, 297), (262, 204),
(271, 206), (243, 184), (276, 132), (276, 114),
(259, 92), (285, 76), (253, 56), (253, 19),
(359, 77), (276, 46), (309, 100), (284, 97),
(288, 127), (314, 131), (264, 198), (265, 194),
(274, 244), (278, 276), (317, 324), (364, 313),
(277, 378), (305, 321), (270, 436), (270, 429),
 (313, 477), (311, 527), (263, 505), (263, 657),
 (268, 685), (321, 712), (271, 718), (389, 713),
 (418, 693), (374, 656), (375, 636), (378, 634),
 (394, 620), (371, 577), (414, 540), (417, 508),
 (409, 513), (390, 472), (408, 450), (395, 413),
 (391, 367), (396, 388), (429, 413), (428, 463),
 (411, 469), (424, 525), (428, 543), (431, 573),
 (403, 602), (409, 621), (445, 661), (433, 677),
 (480, 683), (515, 676), (536, 648), (537, 639),
 (547, 575), (532, 572), (555, 523), (542, 503),
 (537, 480), (538, 456), (570, 439), (549, 409),
 (555, 414), (594, 424), (595, 447), (557, 464),
 (596, 499), (602, 501), (589, 550), (589, 555),
 (591, 582)]

lightList = []
lightNum = 0

for light in lightCoords:
    lightList.append([[light[0], light[1]], lightNum])
    lightNum += 1


lightNum = 0
loops = 0
origin = ([[0, 0, 0], [0, 0, 0]])

while loops < 37:
    for light in lightList:
        startingVector = np.array([[light[0][0]], [light[0][1]]])
        rotationMatrix = np.array([[math.cos(math.pi/18), -math.sin(math.pi/18)], [math.sin(math.pi/18), math.cos(math.pi/18)]])
        resUnrounded = np.matmul(rotationMatrix, startingVector)
        res = np.round(resUnrounded, decimals=2)
        lightList[lightNum] = [[res[0][0], res[1][0]], lightNum]
        lightNum += 1
    print(lightList[0][0][0], end=", ")
    print(lightList[0][0][1])
    ax.quiver(lightList[0][0][0], lightList[0][0][1], angles='xy', scale_units='xy', scale=1)
    lightNum = 0
    loops += 1

ratio = 1.0
x_left, x_right = ax.get_xlim()
y_low, y_high = ax.get_ylim()
ax.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)
plt.axis([-1000, 1000, -1000, 1000])
plt.show()
