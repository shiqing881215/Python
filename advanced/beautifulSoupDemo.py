# The url you can try here is http://www.dr-chuch.com/page1.htm

import urllib
# You need to put BeautifulSoup.py in the same folder
from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of anchor tags
tags = soup('a')

for tag in tags :
    print tag.get('href', None)