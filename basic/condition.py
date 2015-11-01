age = raw_input('How old are you? ')
try :
    ageInt = int(age)
    if (ageInt < 10) : 
        print 'You are a kid'
    elif (ageInt > 20) : 
        print 'You are an adult'
    else :
        print 'You are a teenager'
    print 'Done'
except : 
    print 'Your input is not a interger'    


x = raw_input('Give a value to x ')
try :
    xInt = int(x)
    if (xInt == 5) :
        print 'x is 5'
        print 'x is still 5'
        print 'x is still 5 again'
    if (xInt != 5) : 
        print 'x is not 5'
        print 'x is still not 5'
        print 'x is still not 5 again'
except : 
    print 'Your input is not an interger'

