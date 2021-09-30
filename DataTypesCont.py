#string
s = "I am a string."
print(type(s))						#will return string

#boolean
yes = True
print(type(yes))					#will return Boolean True

no = False
print(type(no))						#will return Boolean False

#lists -- ordered and changeable
alpha_list = ["a", "b", "c"]			#list initialization
print(type(alpha_list))						#will return tuple
print(type(alpha_list[0]))				#will return string
alpha_list.append("d")						#will add 'd' to the list end
print(alpha_list)									#will print list

#tuple -- ordered and unchangeable
alpha_tuple = ("a", "b", "c")			#tuple initialization
print(type(alpha_tuple))					#will return tuple

try:															#attempts to execute following line
	alpha_tuple[2] = "d"						#won't work; will raise TypeError
except TypeError:																	#
	print("Element[s] cannot be added to a tuple.")	#
print(alpha_tuple)
