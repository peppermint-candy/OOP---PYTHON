class MathDojo(object):
	"""docstring for MathDojo"""
	def __init__(self, num, num1,num2):
		self.num = 0
		self.num1 = num1
		self.num2 = num2
	def add(self,num, num1,num2):
		self.num += int(self.num1) + int(self.num2)
		return self
	def subtract(self,num1,num2):
		self.num -= int(self.num1) + int(self.num2)
		return self
	def result():
		print str(self.num)
