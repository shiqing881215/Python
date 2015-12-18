class PartyAnimal :
	x = 0
	name = ""

	# This is the constructor
	def __init__(self, name) :
		self.name = name
		print "I'm constructing", self.name

	# method, each python class at least has one variable called self
	def party(self):
		self.x = self.x+1
		print self.name, " says ", self.x

	# This is the destructor
	def __del__(self):
		print "I'm destructed", self.name

# Attention - there is no "new" keyword
jack = PartyAnimal("Jack")
rose = PartyAnimal("Rose")
jack.party()
jack.party()
jack.party()
rose.party()
jack.party()
rose.party()

'''
The result is 

I'm constructing Jack
I'm constructing Rose
Jack  says  1
Jack  says  2
Jack  says  3
Rose  says  1
Jack  says  4
Rose  says  2
I'm destructed Rose
I'm destructed Jack
'''
