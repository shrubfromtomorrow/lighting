import subprocess
import sys
import os


######## Code for pixeled lighting


# file = sys.argv[1]

# run = ["python3", f"{file}"]
# scp = ["scp", "/home/orion/Code/Python/2DLighting/lightOrder.txt", "pi@192.168.10.223:"]
# scp2 = ["scp", "/home/orion/Code/Python/2DLighting/lightParse.py", "pi@192.168.10.223:"]
#
# run1 = ["ssh", "pi@192.168.10.223", f"sudo python3 lightParse.py"]
#
# os.chdir("/home/orion/Code/Python/2DLighting/LightingPatterns/")
# subprocess.run(run)
# subprocess.run(scp2)
# subprocess.run(scp)
# subprocess.run(run1)
#

######## Code for ligthing pattern


file = sys.argv[1]

run = ["python3", f"{file}"]
scp = ["scp", "/home/orion/Code/Python/2DLighting/lightOrder.txt", "pi@192.168.10.223:"]
scp2 = ["scp", "/home/orion/Code/Python/2DLighting/lightParse.py", "pi@192.168.10.223:"]

run1 = ["ssh", "pi@192.168.10.223", f"sudo python3 lightParse.py"]

os.chdir("/home/orion/Code/Python/2DLighting/LightingPatterns/")
subprocess.run(run)
subprocess.run(scp2)
subprocess.run(scp)
subprocess.run(run1)
