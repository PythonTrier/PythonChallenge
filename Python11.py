# https://pillow.readthedocs.io/en/5.3.x/
from PIL import Image

im = Image.open('cave.jpg')
(height, width) = im.size

evenImage = Image.new('RGB', (int(height / 2), int(width / 2)))
oddImage = Image.new('RGB', (int(height / 2), int(width / 2)))

for inY in range(height):
    for inX in range(width):
        outY = int(inY / 2)
        outX = int(inX / 2)
        p = im.getpixel((inY, inX))

        if (inY + inX) %2 == 1:
            oddImage.putpixel((outY, outX), p)
        else:
            evenImage.putpixel((outY, outX), p)

evenImage.save('evenImage.jpg')
evenImage.close()

oddImage.save('oddImage.jpg')
oddImage.close()
