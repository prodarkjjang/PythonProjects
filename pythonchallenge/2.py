#3 Learn Web Scraping and translate again
# Import Beautiful Soup
import requests
from bs4 import BeautifulSoup
from bs4 import Comment
  
url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))

z = "{}[]!@#$%^&*()+_\n"
mytable = comments[1].maketrans("", "", z)
print(comments[1].translate(mytable))