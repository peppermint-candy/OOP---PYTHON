class Frame(object):
	def __init__(self,height,width):
		self.height = height
		self.width = width
		self.pic = ""
	def __str__(self):
		return "return with height {}, width{}, picture {}".format(self.height,self.width,self.pic)
	def __iter__(self):
	def change_pic(self):
		self.pic = new_pic
		return self

class SquareFrame(Frame):
	"""docstring for SquareFrame"""
	def __init__(self, side_length):
		super(SquareFrame, self).__init__(side_length, side_length)
		self.side_length = side_length

my_frame = Frame(200,200)
frame2 = SquareFrame(100)

my_frame.change_pic("John Adams")


