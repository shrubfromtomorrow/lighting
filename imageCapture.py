import cv2
from time import sleep
import subprocess


light = 0
while light < 100:
    subprocess.run(["ssh", "pi@192.168.10.223", f"sudo python3 lightCapPi.py {light}"])
    cap = cv2.VideoCapture(0)
    ret,frame = cap.read()
    cv2.imwrite(f'Images/Images100Mk2/c{str(light)}.png',frame)
    cap.release()
    light += 1
