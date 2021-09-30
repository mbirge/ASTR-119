'''
this is a multi-line comment
'''
#this is a single line comment

import numpy as np

def main():
	i = 0 #variable 'i' is an integer 'int'	
	n = 10 #second variable 'n' is also an integer
	x = 119.0 #variable 'x' is a floating point number 'float', declared with 'xx.xx'
	
	#numpy can be used to quicky declare arrays
	
	y = np.zeroes(n, dtype=float) #declares zeroes as floats using np
	#'for loops' can be used to iterate with a variable
	
	for i in range(n): # i in range [0, n-1]
		y[i] = 2.0 * float(i) + 1.0 #sets 'y' as a float (2i + 1)
		
		#to iterate through a variable array
	for y_element in y:
		print(y_element)
		
			#execute the main function:	
	if __name__ == "__main__":
				main()
