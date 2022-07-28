import subprocess

file = "lightingX+Y.py"

scp = ["scp", f"/home/orion/Code/Python/2D\ Lighting/LightingPatterns/{file}", "pi@192.168.10.223:"]

run = ["ssh", "pi@192.168.10.223", f"python3 {file}"]

subprocess.run(scp)
subprocess.run(run)
