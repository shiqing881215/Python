fruits = ['apple', 'banana', 'peach']
print fruits
print fruits[0]

# String is immutable but list is
fruit = 'apple'
# fruit[0] = 'A'   This will throw the error
fruits[0] = 'Apple'  # This is fine

print 'Length of fruits is ', len(fruits)

# range() function returns you a list
print range(4)
print range(len(fruits))

# concatenate
newList = [1,2,'haha'] + [[4,6], 'wowo']
print newList

# slice - include start not end
print [1,2,3,4,5,6][1:3]

print type(fruits)
print dir(fruits)

# constructor
cars = list()
cars.append('Honda')
cars.append('Benz')
cars.append('BMW')
print cars

print 1 in [1,2,3]
print 1 not in [1,2,3]

# Sort - change the list itself
unsorted = [45,1,55,89,100,3]
unsorted.sort()
print unsorted

# Other functions
print max(unsorted)
print min(unsorted)
print sum(unsorted)

# Split
abc = 'with three words'
abcList = abc.split()
print abcList, len(abcList)

abc2 = 'with;three;words'
abcList2 = abc2.split(';')
print abcList2, len(abcList2)
