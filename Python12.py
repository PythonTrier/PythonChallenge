formats=['jpg', 'png', 'gif', 'png', 'jpg']

f=open('evil2.gfx', 'rb')
filedata=f.read()
f.close()

for i in range(5):
    f=open('evil2_'+str(i)+'.'+formats[i], 'wb')
    f.write(filedata[i::5])
    f.close()