numbers = (1,2,3)
print numbers
print max(numbers)
print len(numbers)
for number in numbers : 
    print number

t = tuple()
print dir(t)

# You can do assignment on both sides
(x,y) = (4, 'fred')
print x, y

# Compare - compare the first then the second and etc
print (1,2,3) < (9,0,0)
print (1,2,3) > (1,2,2)
print (1,2,3) == (1,2,3)

# Since it's comparable, so tuples can be sorted
ts = [('b', 1), ('c', 30), ('a', 10)]
print ts
ts.sort()
print ts
ts.sort(reverse=True)
print ts

# Use built-in sorted() method
d = {'b' : 1, 'a' : 10, 'c' : 30}
print sorted(d.items())

# Sort on value instead of key
d = {'b' : 1, 'a' : 10, 'c' : 30}
tmp = list()
for k,v in d.items() : 
    tmp.append( (v,k) )
print tmp
tmp.sort(reverse=True)  # Show most frequent
print tmp

# Short version
# List comprehension creates a dynamic list
d = {'b' : 1, 'a' : 10, 'c' : 30}
print sorted( [(v,k) for (k,v) in d.items()] )