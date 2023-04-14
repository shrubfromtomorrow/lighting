import subprocess
import os

print("This script will take photos of neopixel LEDs in sequence and output images with their brightest pixel selected.")

ip = input("Please enter the IP address of your Raspberry Pi, e.g., 192.168.1.1: ")

output = subprocess.check_output(['python3', f'imageCapture.py', ip])

print(f"The images are now ouputted in the Images directory, named {output}. Please check framing now.")

def processIms():
    process = input("Would you like to go through all of the images and get the brightest pixel? This will also create a directory in Images/CircImages with outputted images. [y/n] ")
    if process == "y":
        subprocess.run(["python3", f"imageProcessing.py", output])
    elif process == "n":
        quit()
    else:
        print("Bad input")
        processIms()

processIms()

print("The images with the brightest pixel circled are now outputted. The coordinates of the brightest pixel in each image are in \"lightCoords.txt\"")