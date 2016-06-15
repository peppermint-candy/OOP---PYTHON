# import the library
	#import urllib
	#python2.x import urllib28
# use it
	#urllib.urlopen(...)

	# Writing your own Python modules is very simple. To create a module, we first create a new .py file with the module name in the same directory as the file that will import the module. Then we import it using the import command and the Python file name (without the .py extension)

	#file name: arithmetic.py
# def add(x, y):
#     return x + y
# def multiply(x, y):
#     return x * y
# def subtract(x, y):
#      return x - y

import arithmetic
print arithmetic.add(5, 8)
print arithmetic.subtract(10, 5)
print arithmetic.multiply(12, 6)