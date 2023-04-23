# This is the main program for executing lighting code

import subprocess
import sys
import os


# This function will either display an image or a pattern on the LEDs
def lighting():
    patternBool = int(input("Would you like to display a pattern (1) or a process an image (2)?: "))

    if patternBool == 1:
        pattern = input("Please input the absolute directory to the pattern you wish to display: ")
        ip = input("Please enter the IP address of your Raspberry Pi: ")
        delay = float(input("Please select a delay time between each frame of the pattern (should it be an animation): "))
        loops = int(input("How many times do you want this to loop, if at all?: "))

        # The following commands copy the pattern and light coordinates to a Raspberry Pi and run the pattern

        scpPattern = ["scp", f"{pattern}", f"pi@{ip}:"]
        scpCoords = ["scp", "lightCoords.txt", f"pi@{ip}:"]
        run = ["ssh", f"pi@{ip}", f"sudo python3 {pattern} {delay} {loops}"]

        subprocess.run(scpPattern)
        subprocess.run(scpCoords)
        subprocess.run(run)

    elif patternBool == 2:
        ip = input("Please enter the ip address of your Raspberry Pi: ")
        delay = float(input("Please select a delay time between each frame of the pixeled image(s) (should it be an animation): "))
        loops = int(input("How many times do you want this to loop, if at all?: "))

        run = ["python3", "pixeling.py"]
        scpOrder = ["scp", "lightOrder", f"pi@{ip}:"]
        scpParse = ["scp", "lightParse.py", f"pi@{ip}:"]
        lightUp = ["ssh", f"pi@{ip}", f"sudo python3 lightParse.py {delay} {loops}"]

        # The following commands run pixeling.py to output to lightOrder, copies lightOrder to the Raspberry Pi, copies the parsing code, and runs the parsing code

        subprocess.run(run)
        subprocess.run(scpOrder)
        subprocess.run(scpCoords)
        subprocess.run(lightUp)

    else:
        print("That is not an input I am familiar with, please try again")
        lighting()

lighting()

# file = sys.argv[1]

# ip = sys.argv[2]

# delay = sys.argv[3]

# loops = sys.argv[4]

# run = ["python3", f"{file}"]
# scp = ["scp", "/home/orion/Code/Python/2DLighting/lightOrder", f"pi@{ip}:"]

# scp2 = ["scp", f"/home/orion/Code/Python/2DLighting/lightParse.py", f"pi@{ip}:"]

# run1 = ["ssh", f"pi@{ip}", f"sudo python3 lightParse.py {delay} {loops}"]

# # os.chdir("/home/orion/Code/Python/2DLighting/LightingPatterns/")
# subprocess.run(run)
# subprocess.run(scp)
# subprocess.run(scp2)

# subprocess.run(run1)

