#6 learn how to use zipfile
# at first, thought it was related to zip() function
# turns out i should change url to .zip to download file
# found readme and then found "Collect the comments"
# supposed to use zipfile but mac auto unzips
# change to manual unzip and solved

import re
import os
import zipfile

cur = 90052
f = zipfile.ZipFile("./channel.zip")
result = ""


while 1:
    filename = str(cur) + ".txt"
    body = f.read(filename).decode("utf-8")
    comment = f.getinfo(filename).comment.decode("utf-8")
    result += comment
    # print(body)
    # print(comment)
    num = re.findall('[0-9]+', body)
    if num:
        # print(num[-1])
        cur = num[-1]
    else:
        break
f.close()
print(result)