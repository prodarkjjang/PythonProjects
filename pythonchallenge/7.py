#7 pillow
# found pillow while googling for image process and got partially spoilt on google result description
# crop out the row of colors and get each pixel code by remove duplicating neighbours
# convert them to ascii letters
# realise duplicate neighbour method wont work as there could be legit same neighbouring color
# use fix distance instead

from PIL import Image
im = Image.open("oxygen.png")
# im.show()

box = (0, 49, 608, 50)
region = im.crop(box)
# region.show()

pixels = list(region.getdata())
# print(pixels)
arr = []
for i in range(0, len(pixels), 7):
    print(pixels[i][0])
    arr.append(pixels[i][0])
# print(arr)

# # image decrypted
solution1 = "".join(list(map(chr, arr)))
print(solution1)

puzzle2 = [105, 110, 116, 101, 103, 114, 105, 116, 121]

print("".join(list(map(chr, puzzle2))))

