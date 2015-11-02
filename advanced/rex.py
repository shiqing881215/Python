import re

#search demo, return true / false
line = "This is an email from Jetty"

if re.search("This", line) :
    print "Yes, include 'This'"

if re.search("^This", line) :
    print "Yes, start with 'This'"

# * mean 0 - many times
if re.search("^T.*", line) :
    print "Yes, start with T and following by any character"

# + means 1 - many times
if re.search("^T.+", line) :
    print "Yes, start with T and following by at least one character"

# \S means none-blank char
if re.search("^T\S+", line) :
    print "Yes, start with T and following by at least one none-blank character"


# findall demo, return a list of matching results
line2 = "My favorite number is 19 and 42"

print re.findall("[0-9]+", line2)


# By default, python does the greedy matching, which means get larger one
line3 = "From: jetty's email: j@t.com"

# This will print the ["From: jetty's email:"]  which tries to get the last :
print re.findall("^F.+:", line3)  

# This will print ["From:"] which is turn off default greedy setting
print re.findall("^F.+?:", line3) 

# This is to extract the email address
print re.findall("\S+@\S+", line3)


# Sometimes, we want to match something, but don't want to extract all the matched stuff
# So we can use (), it will only return the stuff inside of ()
line4 = "From a@b.com saying hello"

# It will match "From a@a.com", but will only return "a@a.com"
print re.findall("^From (\S+@\S+)", line4)

# Extract the domain name
print re.findall("@(\S*)", line4)
print re.findall("@([^ ]*)", line4)

