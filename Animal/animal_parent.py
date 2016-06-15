class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name):
		self.name = name
		self.health = 100
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print str(self.name) + " health is " + str(self.health)
		# super(Animal, self).__init__()
		# self.arg = arg

# animal = Animal("Pony")
# animal.walk()
# animal.walk()
# animal.walk()
# animal.run()
# animal.run()
# animal.displayHealth()

class Dragon(Animal):
	"""docstring for Dragon"""
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170
	def fly(self):
		self.health -= 10
		return self
	def disHealth(self):
		print "this is a dragon!"
		self.displayHealth()
		return self
Pet = Animal("Pony")
Pet.walk().walk().run().displayHealth()

Pony = Dragon("Anny")
Pony.fly().fly().disHealth()


