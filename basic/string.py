fruit = 'banana'
print fruit[0]
print len(fruit)

index = 0
while index < len(fruit) :
    print str(index) + " : " + fruit[index]
    index = index + 1

for letter in fruit : 
    print letter

# slice - include beginning/exclude ending
print fruit[0:4]
print fruit[5:6]
print fruit[0:100]  # This returns 'banana'
print fruit[4:0]  # This returns nothing
print fruit[:4]  # This equals to [0:4]
print fruit[2:]  # This equals to [2:6]
print fruit[:]   # This equals to [0:6]

# in operator
if 'a' in fruit : 
    print 'fruit has char a'

# comparison
if 'apple' < fruit :
    print 'apple is smaller'
if 'banana' == fruit :
    print 'fruit is banana'
print 'The first n in fruit is ' + str(fruit.find('n'))

# string library
print 'BANANA lowercase is ' + 'BANANA'.lower()
print 'This is the built in method you can call on string ' + str(dir(fruit))