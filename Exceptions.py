#python exceptions allow you to deal with unexpected results

try:
	print(a)					#a is not defined; will throw an exception
except:
	print("'a' is not defined.")
	
#there are specific errors to help with specific cases
try:
	print(a)
except NameError:
	print("'a' is still not defined.")
except:
	print("Something else went wrong.")
	
	#this will break the program as 'a' is not defined.
	
	print(a)
