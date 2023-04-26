import cv2
import os
import sys
import paramiko
import time
import numpy as np
import matplotlib.pyplot as plt

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(sys.argv[1], username='pi', password='raspberry')
ssh_shell = ssh.invoke_shell()

currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

parentDirectory = "Images/"
imageDir = os.path.join(parentDirectory, currentTime)
os.mkdir(imageDir)



latestFrame = None

light = 0
cap = cv2.VideoCapture(0)

cap.retrieve()
cap.retrieve()
cap.retrieve()

while light < 300:
    command = f"sudo python3 lightCapPi.py {light}\n"
    ssh_shell.send(command)

    # Wait for signal from pi that light is ready
    while True:
        output = ssh_shell.recv(1024).decode()
        if "Ready for picture" in output:
            print(output)
            
            break

    # Take picture
    ret, frame = cap.read()
    print(ret)
    cv2.imwrite(f'{os.path.join(imageDir, str(light))}.jpg', frame)
    latestFrame = frame
    plt.imshow(frame, cmap='gray')
    # plt.show()
    plt.imshow(latestFrame, cmap='gray')
    plt.show()
    light += 1

ssh.close()
cap.release()

print(currentTime, end="")




# st = time.time()
# light = 0
# while light < 300:
#     # subprocess.run(["ssh", "pi@192.168.10.223", f"sudo python3 lightCapPi.py {light}"])
#     subprocess.run(["ssh", "pi@192.168.10.202", f"sudo python3 lightCapPi.py {light}"])
#     cap = cv2.VideoCapture(1)
#     ret,frame = cap.read()
#     cv2.imwrite(f'Images/ImagesTest/c{str(light)}.jpg',frame)
#     cap.release()
#     light += 1