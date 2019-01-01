from PIL import Image
import urllib.request

base_url = "http://www.pythonchallenge.com/pc/def/oxygen.html"

# Download File
x = urllib.request.urlopen(base_url)

img = Image.open('oxygen.png')
pxbuffer = img.load()

output = ""
for x in range(2, 609, 7) :
    output += chr(pxbuffer[x, 47][0])

print(output)