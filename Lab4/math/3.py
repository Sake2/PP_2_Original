import math
n = int(input("Input number of sides "))
L = int(input("Input the lengh of a side "))
print("The area of the polygon is ", L**2 * (n/4) // math.tan(math.radians(180/n)) )