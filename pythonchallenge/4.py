#4 learn to use urllib and regex
# realise there could be 4 numbers, use regex instead of last 5 elements
# at 16044, "Yes. Divide by two and keep going."
# at 82682, "There maybe misleading numbers in the text. One example is 82683. Look only for the next nothing and the next nothing is 63579", get last result instead of first
import urllib.request
import re

nothing = 12345
nothing = 16044 / 2
nothing = 61287
nothing = 66831 # the last one
for i in range(400):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(nothing)
    request_url = urllib.request.urlopen(url)
    body = request_url.read().decode('utf-8')
    print(body)

    num = re.findall('[0-9]+', body)
    # # nothing = int(body[-5:])
    nothing = num[-1]