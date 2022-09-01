from time import sleep
from random import randint
import sys
import math

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

columnDivisor = ((xS[-1][0]+1) - xS[0][0])/10
rowDivisor = ((yS[-1][0]+1) - yS[0][0])/15

columns = []
rows = []

for num in range(0, 10):
    columns.append([])
for num in range(0, 14):
    rows.append([])

for value in xS:
    if xS[0][0] <= value[0] < int((xS[0][0]+(columnDivisor*1))):
        columns[0].append(value[1])
    elif xS[0][0] <= value[0] < int((xS[0][0]+(columnDivisor*2))):
        columns[1].append(value[1])
    elif xS[0][0] <= value[0] < int((xS[0][0]+(columnDivisor*3))):
        columns[2].append(value[1])
    elif xS[0][0] <= value[0] < int((xS[0][0]+(columnDivisor*4))):
        columns[3].append(value[1])
    elif xS[0][0] <= value[0] < int((xS[0][0]+(columnDivisor*5))):
        columns[4].append(value[1])
    elif xS[0][0] <= value[0] < int((xS[0][0]+(columnDivisor*6))):
        columns[5].append(value[1])
    elif xS[0][0] <= value[0] < int((xS[0][0]+(columnDivisor*7))):
        columns[6].append(value[1])
    elif xS[0][0] <= value[0] < int((xS[0][0]+(columnDivisor*8))):
        columns[7].append(value[1])
    elif xS[0][0] <= value[0] < int((xS[0][0]+(columnDivisor*9))):
        columns[8].append(value[1])
    elif xS[0][0] <= value[0] < int((xS[0][0]+(columnDivisor*10))):
        columns[9].append(value[1])
for value in yS:
    if yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*1))):
        rows[0].append(value[1])
    elif yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*2))):
        rows[1].append(value[1])
    elif yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*3))):
        rows[2].append(value[1])
    elif yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*4))):
        rows[3].append(value[1])
    elif yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*5))):
        rows[4].append(value[1])
    elif yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*6))):
        rows[5].append(value[1])
    elif yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*7))):
        rows[6].append(value[1])
    elif yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*8))):
        rows[7].append(value[1])
    elif yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*9))):
        rows[8].append(value[1])
    elif yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*10))):
        rows[9].append(value[1])
    elif yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*11))):
        rows[10].append(value[1])
    elif yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*12))):
        rows[11].append(value[1])
    elif yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*13))):
        rows[12].append(value[1])
    elif yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*14))):
        rows[13].append(value[1])
    elif yS[0][0] <= value[0] < int((yS[0][0]+(columnDivisor*15))):
        rows[14].append(value[1])
