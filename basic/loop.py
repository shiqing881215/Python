def printDelimeter() :
    print ''
    print '---------------------------------------'
    print ''


times = raw_input('How many times do you want to loop ? ')
intTimes = int(times)
while intTimes > 0 :
    print intTimes
    intTimes = intTimes - 1

printDelimeter()

while True : 
    print 'Only when you tyle "Done", then I will finish myself. And if you enter "Skip", I will skip once for you.'
    line = raw_input('Enter your answer : ')
    if (line == 'Done') :
        break
    elif (line == 'Skip') :
        continue
    else : 
        print line
print 'Done'

printDelimeter()

for i in [5,4,3,2,1] :
    print i
