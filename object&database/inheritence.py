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

# This is how to do the "extends"
class FootballFan(PartyAnimal) :
	points = 0

	def touchdown(self) :
		self.points = self.points + 7
		self.party()
		print self.name, "Points ", self.points

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()


'''
The result is 

I'm constructing Sally
Sally  says  1
I'm constructing Jim
Jim  says  1
Jim  says  2
Jim Points  7
I'm destructed Jim
I'm destructed Sally
'''