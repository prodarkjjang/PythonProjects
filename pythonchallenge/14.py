# 14 learn about iterating in directions
# <!-- remember: 100*100 = (100+99+99+98) + (...  -->
# <img src="wire.png" width="100" height="100">
# Found out that 100 * 100 = (100*99) + 100 = (99*99) + 100 + 99 = ...
# 100*100 = 100 + 2*99 + 2*98 + ... + 2*1
# we scan around the pixel in spiral mode

from PIL import Image
im = Image.open("wire.png") 
im2 = Image.new(mode="RGB", size=(100, 100))

w, h = im.size

# print(w, h)
# arr = []
# for x in range(w):
#     pixel = im.getpixel((x, 0))
#     print(pixel)
#     arr.append(pixel)

# im2.show() 

v = [(1, 0), (0, -1), (-1, 0), (0, 1)]

s = 0
length = 100
count = 0
cur = [-1, 0]
minus = True

while length:
    for i in range(length):
        cur = [x + y for x, y in zip(cur, v[s])]
        pixel = im.getpixel((count, 0))
        im2.putpixel(cur, pixel)
        count += 1
    s = (s + 1) % 4
    
    if minus:
        length -= 1
    minus = not minus

im2.show()