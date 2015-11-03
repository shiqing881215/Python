import urllib

# These will be more useful in the daily life than socket library
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fhand :
    print line.strip()