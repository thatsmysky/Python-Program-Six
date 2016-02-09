# Lucy Kull
# Computer Science 101
# Professor Hare
# Program 6 Algorithm

import math

###########################################
####        IMPORTANT VALUES           ####
###########################################
Color_Vectors = {"RED": [255, 0, 0], "GREEN": [0, 255, 0], "BLUE": [0, 0, 255], "BLACK": [0, 0, 0],
                 "WHITE": [255, 255, 255]}
new_picture = []

###########################################
####            FUNCTIONS              ####
###########################################


def try_open(file):
    # noinspection PyBroadException
    try:
        open(file)
    except IOError:
        return False
    except:
        return False
    # Check if the file name ends in .ppm
    if ".ppm" not in file:
        return False
    return True


def check_lines(file):
    # Check if the first line of the file contains P3
    # Check if the third line of the file is 255
    open_file = open(file)
    test_lines = open_file.readlines()
    if "P3" not in test_lines[0]:
        return False
    if "255" not in test_lines[2]:
        return False
    return True


def try_write(file):
    try:
        open(file, 'w')
    except IOError:
        return False
    except:
        return False
    # Write each pixel in the new file:
    # First line of file == P3
    # Second line of file == Second line of original file
    # Third line of file == 255
    # Use the coordinates we modified in the previous section
    # Each pixel component is a line
    return True


def actually_write(out):
    write_file = open(out, 'a')
    for line in new_picture:
        write_file.write(str(line) + '\n')
    write_file.close()


def convert(file, out):
    file = open(file)
    out = open(out, 'w')
    out.write(file.readline())
    out.write(file.readline())
    out.write(file.readline())
    read_file = file.readlines()
    list_of_lines = [j.strip() for j in read_file]
    # Iterate through the file, starting at line 4, each following group of 3 lines is a pixel:
    k = 5
    global new_picture
    while k <= len(list_of_lines):
        RGB = [list_of_lines[k - 2], list_of_lines[k - 1], list_of_lines[k]]
        new_color = euclidean_distance(RGB)
        new_picture += Color_Vectors[new_color]  # list of lists
        k += 3
    file.close()


def euclidean_distance(color):
    color_dict = {}
    # First line is Red
    # Second line is Green
    # Third line is Blue
    RED = int(color[0])
    GREEN = int(color[1])
    BLUE = int(color[2])
    # Use distance formula to determine which color the pixel is closest to
    red_dist = ((255 - RED)**2 + (0 - GREEN)**2 + (0 - BLUE)**2)
    green_dist = ((0 - RED)**2 + (255 - GREEN)**2 + (0 - BLUE)**2)
    blue_dist = ((0 - RED)**2 + (0 - GREEN)**2 + (255 - BLUE)**2)
    black_dist = ((0 - RED)**2 + (0 - GREEN)**2 + (0 - BLUE)**2)
    white_dist = ((255 - RED)**2 + (255 - GREEN)**2 + (255 - BLUE)**2)
    color_dict['RED'] = math.sqrt(red_dist)
    color_dict['GREEN'] = math.sqrt(green_dist)
    color_dict['BLUE'] = math.sqrt(blue_dist)
    color_dict['BLACK'] = math.sqrt(black_dist)
    color_dict['WHITE'] = math.sqrt(white_dist)
    # Whichever color the pixel is closest to, that is the color the pixel becomes.
    # Repeat for each pixel in the file.
    return min(color_dict, key=color_dict.get)  # Returns string


Run_Program = True
while Run_Program:
    print("Welcome")
    print("Press one of the following:")
    print('')
    print("1. To Reduce Color")
    print("Q. To Quit")
    Reduce = input("==> ")
    Reduce = Reduce.lower()
    # If they press Q:
    # Close the program
    if "q" in Reduce:
        break
    # If they press 1:
    # Ask what file they want to reduce
    if "1" in Reduce:
        Picture_File = input("What picture would you like to edit? ")
        # Check if the file opens
        # If any of the checks come back negative, warn the user and ask again.
        if not try_open(Picture_File):
            print("I'm sorry, that file is not valid.")
            continue
        if not check_lines(Picture_File):
            print("I'm sorry, that is not valid.")
            continue
        if try_open(Picture_File):
            if check_lines(Picture_File):
                # Ask the user what to name the file the image will be saved as.
                Output_File = input("What would you like to save your file as? ")
                # If the file cannot be created, warn user, ask again.
                if not try_write(Output_File):
                    print("I'm sorry, that isn't a valid file type.")
                if try_write(Output_File):
                    print("...writing...")
                    convert(Picture_File, Output_File)
                    actually_write(Output_File)
                    # When writing complete, alert user.
                    print("Writing Complete")
    Run_Program = input("Would you like to convert another file? ")
    Run_Program = Run_Program.upper()
    if "Y" in Run_Program:
        Run_Program = True
    else:
        Run_Program = False