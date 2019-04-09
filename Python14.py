# http://www.pythonchallenge.com/pc/return/italy.html

from PIL import Image

directions = [
    (1,0), # move right
    (0, 1), # move down
    (-1, 0), # move left
    (0, -1) # move up
]

outx = 0
outy = 0

direction = 0
paintstep = 0
paintlength = 100

imgin = Image.open('wire.png')
imgout = Image.new('RGB', (100, 100))

for idx in range(10000):
    paintstep = paintstep + 1
    pixel = imgin.getpixel((idx, 0))
    imgout.putpixel((outx, outy), pixel)
    if paintstep == paintlength:
        if direction % 2 == 0:
            paintlength = paintlength - 1
        direction = (direction + 1) % 4
        paintstep = 0
        # print('idx: ' + str(idx))
        # print('outx: ' + str(outx) + ' outy: ' + str(outy))
    outx = outx + directions[direction][0]
    outy = outy + directions[direction][1]

imgout.save('swirl.png')
imgout.close()
imgin.close()

# Version 2
#http://www.pythonchallenge.com/pc/return/italy.html

from PIL import Image

filename='wire.png'
img = Image.open(filename)
width, height = img.size
newimg = Image.new('RGB', (100,100))

directions = [(1,0), (0,1), (-1,0), (0,-1)]
x, y = -1, 0
length = 100
pixel = -1
n=0
while length > 1:
    for direction in directions:
        if n%2 == 1: length -= 1
        n += 1
        for i in range(length):
            x += direction[0]
            y += direction[1]
            pixel += 1
            newimg.putpixel((x,y), img.getpixel((pixel,0)))
newimg.show()
newimg.save('wire_out.png')
newimg.close()
img.close()