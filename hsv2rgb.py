import colorsys
import math
def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
loops = 0
while loops < 10:
    loopsDec = loops/10
    print(loopsDec + 0.1)
    rgb = hsv2rgb(0.1 + (loopsDec), 1, 1)
    print(rgb)
    loops += 1
