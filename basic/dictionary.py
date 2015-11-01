purse = dict()
purse['money'] = 12
purse['candy'] = 5
purse['tissues'] = 3
print purse
print purse['candy']
purse['candy'] = purse['candy'] + 2
print purse

purse2 = {'money':1, 'candy':2, 'tissues':3}
print purse2

print 'money' in purse2
# print purse2['random']   This will give the traceback error

# Second param is the default value which will be used if the key is not found
print purse2.get('money', -1)
print purse2.get('random', -1)

# Loop
for key in purse2 :
    print key, purse2[key]

print list(purse2)
print purse2.keys()
print purse2.values()
print purse2.items()

# Two iteration variable
for key,value in purse2.items() : 
    print key, value

