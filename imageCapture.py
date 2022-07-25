import cv2
from time import sleep
import board
import neopixel

pixels = neopixel.NeoPixel(board.18, 50, brightness = 1)


light = 0
while lights < 50:
    pixels[light].fill((255, 255, 255))
    pixels.show()
    sleep(1)
    cap = cv2.VideoCapture(0)
    ret,frame = cap.read()

    cv2.imwrite(f'Images/c{str(light)}.png',frame)
    cap.release()
    light += 1
    sleep(.25)
