import math
def Spiral(loops, points):
    loopRads = loops * (2*math.pi)
    pointLocsRads = []
    for point in range(1, points+1):
        pointLocsRads.append((loopRads / points)*point)
    radi = []
    for radian in pointLocsRads:
        radi.append(6*radian)
    pointsLocs = []
    pointNum = 0
    for radius in radi:
        x = round(math.cos(pointLocsRads[pointNum]) * radius, 3)
        y = round(math.sin(pointLocsRads[pointNum]) * radius, 3)
        pointsLocs.append([x, y])
        pointNum += 1
    return pointsLocs
print(Spiral(4, 100))
