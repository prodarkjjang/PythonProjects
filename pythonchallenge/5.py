#5 learn pickle function and extract image
# assume something to do with peak - a value bigger than neighbor
# peak hell sounds familiar?? found banner.p - turns out its 'pickle'
# should i use numpy or matplotlib here to iterate faster?

import requests
import pickle
import io

response = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')

with open("response.txt", "w") as f:
    f.write(response.text)
f.close()

infile = open("response.txt",'rb')
unload = pickle.load(infile)
infile.close()

row = ""
for i in unload:
    for sec in i:
        row += sec[0] * sec[1]
    print(row)
    row = ""