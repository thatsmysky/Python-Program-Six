# Python-Program-Six
Converts PPM files to JPG, includes: ppm files, completed jpg files, bad input files for error handling
Program 6 Algorithm

Print Menu:

  	“Welcome…”

  	“Press one of the following”

  	“1. To Reduce Color”

  	“Q. To Quit”

If they press Q:

  	Close the program

If they press 1:

  	Ask what file they want to reduce

Check if the file opens

Check if the first line of the file contains P3

Check if the third line of the file is 255

If any of the checks come back negative, warn the user and ask again.

Ask the user what to name the file the image will be saved as.  

If the file cannot be created, warn user, ask again.


Iterate through the file, starting at line 4, each following group of 3 lines is a pixel:

  	First line is Red

  	Second line is Green

  	Third line is Blue

Use distance formula to determine which color the pixel is closest to (RED = (255,0,0) GREEN = (0,255,0) BLUE = (0,0,255) BLACK = (0,0,0) WHITE = (255,255,255))

Whichever color the pixel is closest to, that is the color the pixel becomes.  

Repeat for each pixel in the file.  


Write each pixel in the new file:

  	First line of file == P3

  	Second line of file == Second line of original file

	  Third line of file == 255

  	Use the coordinates we modified in the previous section

  	Each pixel component is a line


When writing complete, alert user. 

Close files.  

Print Menu (REPEAT PROGRAM)
