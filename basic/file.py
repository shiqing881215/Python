fhandle = open('sampleFile.txt', 'r')  # default mode is read, so you can also omit it
print fhandle
print type(fhandle)

count = 0
for line in fhandle :
    print line
    count = count + 1
print 'Line Count : ', count

# Read the whole file into a string
# Attention, we nee to open the file again - I guess either last time we close it after we read it, or fhanlde reach the end?
fhandle = open('sampleFile.txt', 'r') 
wholeFile = fhandle.read();
print len(wholeFile)
print wholeFile

# Search in a file
fhandle = open('sampleFile.txt', 'r') 
for line in fhandle :
    line = line.rstrip()   # remove the ending newline symbol  (right strip)
    if line.startswith('I just') :
        print line

# Handle bad file name
fname = raw_input('Enter file name')
try :
    fhandle = open(fname)
except : 
    print 'Bad file name'
    exit()
print fhandle


