import xml.etree.ElementTree as ET

data = '<person><name>Chuck</name><phone type="intl">+1 222 333 4444</phone><email hide="yes"/></person>'

tree = ET.fromstring(data)
print 'Name:', tree.find('name').text
print 'Attr:', tree.find('email').get('hide')


data2= '<stuff><users><user x="2"><id>011</id><name>Chuck</name></user><user x="7"><id>061</id><name>John</name></user></users></stuff>'

stuff = ET.fromstring(data2)
list = stuff.findall('users/user')
print 'User count', len(list)
for user in list :
    print 'Name', user.find('name').text
    print 'Id', user.find('id').text
    print 'Attr', user.get('x')