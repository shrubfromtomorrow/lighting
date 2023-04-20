import subprocess
import sys
import os



file = sys.argv[1]

ip = sys.argv[2]

delay = sys.argv[3]

loops = sys.argv[4]

run = ["python3", f"{file}"]
scp = ["scp", "/home/orion/Code/Python/2DLighting/lightOrder", f"pi@{ip}:"]

scp2 = ["scp", f"/home/orion/Code/Python/2DLighting/lightParse.py", f"pi@{ip}:"]

run1 = ["ssh", f"pi@{ip}", f"sudo python3 lightParse.py {delay} {loops}"]

# os.chdir("/home/orion/Code/Python/2DLighting/LightingPatterns/")
subprocess.run(run)
subprocess.run(scp)
subprocess.run(scp2)

subprocess.run(run1)

