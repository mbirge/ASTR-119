x = [0.0, 3.0, 5.0, 2.5, 3.7]							#define an array
print(type(x))

#remove element 3
x.pop(2)
print(x)

#remove the element with a value equal to 2.5
x.remove(2.5)
print(x)

#add an element at the end
x.append(1.2)
print(x)

#copy the array
y = x.copy()
print(y)

#check how many elements have a value equal to 0.0
print(y.count(0.0))

#print the index with a value of 3.7
print(y.index(3.7))

#sort the array
y.sort()
print(y)

#reverse-sort
y.reverse()
print(y)

#remove all elements
y.clear()
print(y)
