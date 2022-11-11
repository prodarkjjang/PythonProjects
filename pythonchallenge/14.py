# 14
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
