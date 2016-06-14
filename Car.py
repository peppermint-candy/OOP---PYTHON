class Car(object):
	"""docstring for Car"""
	def __init__(self, price,speed,fuel,mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel	
		self.mileage = mileage
		self. tax = 0
		self.display_all()
	def display_all(self):
		print "Price: " + str(self.price)
		print "Speed: " + str(self.speed) + "mph"
		print "Fuel: " + str(self.fuel)
		print "Mileage: " + str(self.mileage)
		if int(self.price) > 10000:
			print "Tax: 0.15"
		else: 
			print "Tax: 0.12"

motor1 = Car(12000,35,"Full",15)
# motor1.display_all()