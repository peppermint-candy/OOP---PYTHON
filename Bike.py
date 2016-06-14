class Bike(object):
	"""docstring for bike"""
	def __init__(self, price, max_speed):
		self.max_speed = max_speed
		self.price	= price
		self.totalMiles = 0

		print  "Price is: ", self.price," Max speed is: ", self.max_speed
	def displayInfo(self):
		if self.totalMiles > 0:
			print "Price is: ", self.price," Max speed is: ", self.max_speed, " Total miles: ", self.totalMiles
		else: 
			print "Price is: ", self.price," Max speed is: ", self.max_speed, " Total miles: ", 0

	def ride(self):
		print "Riding"
		self.totalMiles += 10
		return self
	
	def reverse(self):
		print "Reversing"
		self.totalMiles -= 5
		return self

bike1 = Bike("200","25mph")
# bike1.ride()
# bike1.ride()
# bike1.ride()
# bike1.reverse()
# bike1.displayInfo()

#channing method
bike1.ride().ride().ride().reverse().displayInfo()


		