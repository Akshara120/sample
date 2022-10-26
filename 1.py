import math
a=int(input("base:"))
b=int(input("height:"))
c=int(input("altitude:"))
s=a+b+c/2
m=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area:",m)