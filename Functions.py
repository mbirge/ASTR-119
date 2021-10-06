import numpy as np
import sys

#define a function that returns a value
def expo(x):
	return np.exp(x)	#return the np e^x (natural exponent) function
	
#define a subroutine that does NOT return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))		#calls the expo function
		
#define the main function
def main():
	n = 10	#provide default value of n
	
	#check for command line argument
	if(len(sys.argv)>1): #if argument was provided, use as value for n
		n = int(sys.argv[1])
		
	show_expo(n)		#call the show_expo subroutine
	
#main function run
if __name__ == "__main__":
	main()
