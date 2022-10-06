import cv2
from time import sleep
import subprocess


light = 0
while light < 10:
    subprocess.run(["ssh", "pi@192.168.1.2", f"sudo python3 lightCapPi.py {light}"])
    cap = cv2.VideoCapture(0)
    ret,frame = cap.read()
    cv2.imwrite(f'Images/ImagesTest/c{str(light)}.png',frame)
    cap.release()
    light += 1
