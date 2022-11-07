#3 Counter and state, (not sure can use window or not)
# attempt 1: fail as my solution catered to at least 3 big letters on both sides
# attempt 2: exactly 3 big letters on left and right, found the first combo, which was l, and got "yes. but there are more."
# change linkedlist.com to linkedlist.php
url = 'http://www.pythonchallenge.com/pc/def/equality.html'
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))

z = "{}[]!@#$%^&*()+_\n"
mytable = comments[0].maketrans("", "", z)
comment = comments[0].translate(mytable)

bigCount = 0
smallCount = 0
solution = ""
for i in range(len(comment)):
    if comment[i].isupper() == False:
        if bigCount != 3:
            smallCount = 0
        elif smallCount == 0:
            smallCount = 1
        elif smallCount == 1:
            print(comment[i-8:i+1])
            solution += comment[i - 4]
        bigCount = 0
    else:
        bigCount += 1
        
print(solution)
