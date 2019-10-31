print ("\t\tfind the value of cos(a-b)")
from math import sin,cos
a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = cos(a)*cos(b)+ sin(a)*sin(b)
print("The value of cos(a-b) is =  ",c)
