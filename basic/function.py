def hello() : 
    print 'Hello'

hello()
print 'and'
hello()

def add(a, b) :
    return a+b

a = raw_input('Enter your first number : ')
b = raw_input('Enter your second number : ')
print 'The addition of these two number is ' + str(add(int(a), int(b)))