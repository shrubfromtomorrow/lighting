import cv2
import os
import paramiko
import time
# import subprocess

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.10.202', username='pi', password='raspberry')
ssh_shell = ssh.invoke_shell()

st = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

parentDirectory = "Images/"
imageDir = os.path.join(parentDirectory, st)
os.mkdir(imageDir)

light = 0
while light < 300:
    command = f"sudo python3 lightCapPi.py {light}\n"
    ssh_shell.send(command)

    while not ssh_shell.recv_ready():
        pass
        time.sleep(0.01)

    cap = cv2.VideoCapture(1)
    ret,frame = cap.read()
    cv2.imwrite(f'{os.path.join(imageDir, str(light))}.jpg',frame)
    cap.release()
    light += 1


ssh.close()
et = time.time()
elapsedTime = et - st
print(f"Elapsed time: {elapsedTime} seconds")



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