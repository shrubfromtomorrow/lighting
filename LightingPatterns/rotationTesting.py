import numpy as np
import math

startingVector = np.array([[1], [1]])

rotationMatrix = np.array([[math.cos(math.pi/18), -math.sin(math.pi/18)], [math.sin(math.pi/18), math.cos(math.pi/18)]])

resUnrounded = np.matmul(rotationMatrix, startingVector)

res = np.round(resUnrounded, decimals=4)

print(res)
