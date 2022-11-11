# 11 splitting odd and even image
# odd and even
# unmerge image into 2 separate image?
# get pixels and filter based on odd or even rgb values?
# so it was really filter based on odd or even coordinates, but dont understand how we end up getting that image

from PIL import Image

im = Image.open("cave.jpeg")
# image.show()
w = 640
h = 480

# ODD EVEN ON PIXEL VALUES
# for x in range(w):
#     for y in range(h):
#         color = im.getpixel((x, y))
#         print(color)
#         c1,c2,c3 = color

#         if c1 % 2:
#             c1 = 0
#         if c2 % 2:
#             c2 = 0
#         if c3 % 2:
#             c3 = 0
        
#         im.putpixel((x,y), (c1,c2,c3))

# im.show()

odd = Image.new('RGB', (w//2, h//2), color=0)
even = Image.new('RGB', (w//2, h//2), color=0)


for x in range(w):
    for y in range(h):
        color = im.getpixel((x, y))
        if x % 2 or y % 2:
            odd.putpixel((x // 2, y // 2), color) 
        elif x % 2 == 0 or y % 2 == 0:
            even.putpixel((x // 2, y // 2), color) 

im.show()
odd.show()
even.show()