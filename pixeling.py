""" This file takes in some number of images and maps individual LEDs to the pixel values of the images """

import math
import cv2
import os
import time

# Open light_coords.txt and reads the coordinates of each light and its light number into a list of length 2
light_coords = []
light_num = 0
with open(r'light_coords', 'r') as coords:
    for line in coords:
        coord = line[:-1]
        light_coords.append([eval(coord), light_num])
        light_num += 1


# This section sorts x and y coords and creates a new 0,0 origin based on light coords not the "top left". Also tracks total pixel distance between maxima and minima
xS = []
yS = []

for light in light_coords:
    xS.append([light[0][0], light[1]])
    yS.append([light[0][1], light[1]])

xS.sort()
yS.sort()

x_dif = xS[-1][0] - xS[0][0]
y_dif = yS[-1][0] - yS[0][0]


# This function takes in a binary file, an image file, and a parent directory of said image and writes the lightorder to binary file
def output_light_order(binary_file, file, parent_dir):

    # Read images and determine width and height
    img = cv2.imread(os.path.join(parent_dir, file))

    try:
        width = img.shape[1]
        height = img.shape[0]

        for light in light_coords:
            
            # This is a calculation of the ratio of the light x and y to the difference between max x and max y. Applying this same ratio to pixel value on image width or height:

            # lightX | ?
            # ------ | ------
            # x_dif   | widthOfIm


            new_x = math.floor((light[0][0]) * (width - 1) / x_dif)
            new_y = math.floor((light[0][1]) * (height - 1) / y_dif)
            
            
            # row then column is the correct order to reference a pixel in opencv
            color = img[new_y, new_x]


            # Write bytes to binary file in big endian order. The light index (light[1]) goes past 256 and this requires two bytes
            binary_file.write(light[1].to_bytes(2, byteorder='big'))
            # Opencv outputs colors as BGR, this is red
            binary_file.write(int(color[2]).to_bytes(1, byteorder='big'))
            # Green
            binary_file.write(int(color[1]).to_bytes(1, byteorder='big'))
            # Blue
            binary_file.write(int(color[0]).to_bytes(1, byteorder='big'))


    except AttributeError:
        print("There is a non-image type file in the directory you have given (make sure you have given the correct path?)")
        exit(0)




# Sort file names by the first number in their name, helps with organizing animations into frames
def sort_files_by_number(filenames):
    # Create a list of tuples with the filename and its number
    file_numbers = [(filename, int(''.join(filter(str.isdigit, filename)))) for filename in filenames]
    
    # Sort the list of tuples by the number
    sorted_file_numbers = sorted(file_numbers, key=lambda x: x[1])
    
    # Create a list of the sorted filenames
    sorted_filenames = [file_number[0] for file_number in sorted_file_numbers]
    
    # Return a tuple of the sorted filenames and numbers
    return sorted_filenames


# Get parent directory of all images
directory = input("What directory would you like to use as a source of input images? (please use absolute paths): ")
file_order = os.listdir(directory)

# Try to sort filenames by number, if there are no numbers, it will output the binary file in default lexicographical order
try:
    file_order = sort_files_by_number(file_order)
    with open("lightOrder", "wb") as binary_file:
        for file in file_order:
            output_light_order(binary_file, file, directory)
        
except ValueError:
    print("File(s) contain no numbers, proceeding in order")

    with open("lightOrder", "wb") as binary_file:
        for file in file_order:
            output_light_order(binary_file, file, directory)