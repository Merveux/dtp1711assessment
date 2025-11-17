x=int(input("Enter the integer:"))
y=float(input("Enter the decimal:"))
z=input("Enter the string:")
print(type(x))
print(type(y))
print(type(z))
list=[x,y,z]
newlist=[str(element) for element in list]
print(newlist)
