import numpy as np			#imports numpy library

#integers

i = 10						#integer
print(type(i))		#prints the datatype of 'i'

a_i = np.zeros(i, dtype=int)			#declare an array of integers
print(type(a_i))									#will return nd array
print(type(a_i[0]))								#will return int64

#floats

x = 119.0					#floating point number
print(type(x))		#prints the datatype of 'x'

y = 1.19e2				#float 119.0 represented in scientific notation
print(type(y))		#prints the datatype of 'y'

z = np.zeros(i,dtype=float)				#declare an array of floats
print(type(z))										#will return nd array
print(type(z[0]))									#will return float64
