#tuple
#ordered, immutable, hetergenous, allow duplicates


#lenth of the tuple
tuple=(20,5,10,25)
print(len(tuple))

#type casting
print(type(tuple))

#copy the tuple into list
x=('apple','mango',20,15)
y=list(x)
print(y)

#changing value
y[1]=6
print(y)

#unpack in tuple
t=('apple','mango','orange')
(red,yellow,orange)=t
print(red)
print(yellow)
print(orange)