# 1
str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def plustwo(letter):
    if ord(letter) < 97 or ord(letter) > 122:
        return letter
    else:
        ascii = ord(letter) + 2
        ascii = ascii if ascii <= 122 else ascii - 26
        return chr(ascii)

print("".join(list(map(plustwo,str))))

# txt = "http://www.pythonchallenge.com/pc/def/map.html"
txt = "map"

x = "abcdefghijklmnopqrstuvwxyz"
y = "cdefghijklmnopqrstuvwxyzab"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))
