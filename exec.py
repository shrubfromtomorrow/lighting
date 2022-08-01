import subprocess
import sys

file = sys.argv[1]

scp = ["scp", f"/home/orion/Code/Python/2DLighting/LightingPatterns/{file}", "pi@192.168.10.223:"]

run = ["ssh", "pi@192.168.10.223", f"sudo python3 {file}"]

subprocess.run(scp)
subprocess.run(run)
