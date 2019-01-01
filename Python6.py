#Used to make requests
import urllib.request
import re
import os
import zipfile
import sys

r = r'[0-9]*$'
base_url = "http://www.pythonchallenge.com/pc/def/channel.zip"

# Download File
x = urllib.request.urlopen(base_url)
# Open the file, give it a name,
download_file = open("channel.zip", 'bw')
# Read the zip file and write the bytes to the channel.zip file
download_file.write(x.read())
download_file.close()

# Unzip file
# Check if the output directory exists.
if not os.path.exists("output"):
   # If not, make it.
   os.makedirs("output")

# Open zip file in read mode.
zip_ref = zipfile.ZipFile("channel.zip", 'r')
# Extract zip file
zip_ref.extractall("output")

commentSum = ""

# Open and printout the readme.txt for the user.
readme = open("output/readme.txt", 'r')
print(readme.read())

# Basic interface to either enter first number or exit.
next_nothing = input("Enter file number or 'exit' to quit: ")
if next_nothing == "exit":
    print("Goodbye!")
    sys.exit()

while next_nothing.isdigit() == True:
    # Open file with given number
    number_file = open("output/{0}.txt".format(next_nothing), 'r')
    # Extract next nothing
    # RegEX Mask
    r = r'[0-9]*$'

    # Converts the number of the current next_nothing to a file name.
    curFile = str(next_nothing) + ".txt"
    commentSum += zip_ref.getinfo(curFile).comment.decode("utf-8")

    previous_nothing = 0
    response_nothing = number_file.read()
    next_nothing = re.findall(r, response_nothing)[0]
    number_file.close()
    # Go to next nothing file

    if next_nothing.isdigit() != True:
        print("STOP! {0}".format(response_nothing))
        print("Your last nothing is: {0}".format(previous_nothing))
        print("Comments : {0}".format(commentSum))
        next_nothing = input("Enter your next nothing or 'exit' to quit: ")
        if next_nothing == "exit":
            print("Goodbye!")
            # break

    else:
        previous_nothing=next_nothing
        print("Next nothing: {0}".format(next_nothing))

#hockey.html

#oxygen.html
