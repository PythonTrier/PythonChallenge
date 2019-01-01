from PIL import Image

img = Image.open('oxygen.png')
pxbuffer = img.load()

output = ""
for x in range(2, 609, 7) :
    output += chr(pxbuffer[x, 47][0])

print(output)


#integrity
