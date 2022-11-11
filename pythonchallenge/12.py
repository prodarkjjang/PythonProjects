#12 learn insane image manipulation
# attempt to split image into individual bands but doesnt seem correct
# trying to separate horizontally and vertically but all wrong
# check hint, apparently got another image 'evil2'
# Run
# curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg
# to see error msg or load at chrome to see error
# key in 'bert' to download another gif file
# split the gfx file into 5 jpg images
# it forms dis, pro, port, ional


from PIL import Image
im = Image.open("evil1.jpeg")
# im.show()

w, h = im.size

red = Image.new('RGB', (w, h), color=0)

paint = True
line = 0

# for y in range(h):
#     if paint:
#         for x in range(w):
#             color = im.getpixel((x, y))
#             red.putpixel((x, y), color) 
    
#     line += 1
#     if line >= 5:
#         line = 0
#         paint = False if paint else True

# im.show()
# red.show()


# for x in range(w):
#     for y in range(h):
#         color = im.getpixel((x, y))
#         if x % 2:
#             red.putpixel((x // 2, y), color)

# im.show()
# red.show()


data = open("evil2.gfx", "rb").read()
print(len(data))

for i in range(5):
    open('%d.jpg' % i ,'wb').write(data[i::5])
