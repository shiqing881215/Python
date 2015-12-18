class PartyAnimal :
	# field
	x = 0
	# method, each python class at least has one variable called self
	# and when you call this method, you don't need to pass the self explicitly
	# the object call the method become the self
	def party(self):
		self.x = self.x+1
		print "So far", self.x

# Attention - there is no "new" keyword
an = PartyAnimal()
an.party()
an.party()
an.party()

print "Type : ", type(an)
print "Dir : ", dir(an)   # This will list both the methods and attributes together