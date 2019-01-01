from PIL import Image
import re

img = Image.open('oxygen.png')
pxbuffer = img.load()

output = ""
output2 = ""
for x in range(1, img.width, 7):
    output += chr(pxbuffer[x, img.height/2][0])

print(output)

numbers = re.findall("\d+", output)

print(numbers)
for x in numbers:
    output2 += (chr(int(x)))

print(output2)

# integrity
