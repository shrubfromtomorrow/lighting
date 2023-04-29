""" This file is used to capture an image of each LED """

import cv2
import os
import sys
import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(sys.argv[1], username='pi', password='raspberry')
ssh_shell = ssh.invoke_shell()

currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

parentDirectory = "Images/"
imageDir = os.path.join(parentDirectory, currentTime)
os.mkdir(imageDir)

light = 0
cap = cv2.VideoCapture(0)
while light < 300:
    command = f"sudo python3 lightCapPi.py {light}\n"
    ssh_shell.send(command)

    # Wait for signal from pi that light is ready
    while True:
        output = ssh_shell.recv(1024).decode()
        if "Ready for picture" in output:
            break

    # Take picture
    ret, frame = cap.read()
    cv2.imwrite(f'{os.path.join(imageDir, str(light))}.jpg', frame)
    light += 1

cap.release()
ssh.close()

print(currentTime, end="")
