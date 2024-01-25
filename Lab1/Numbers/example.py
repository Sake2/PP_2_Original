x = 1    # int
y = 2.8  # float
z = 1j   # complex


print(type(x))  # int
print(type(y))  # float
print(type(z))   # complex


x = 1       # int
y = 35656222554887711   # int
z = -3255522  # int

print(type(x))   # int
print(type(y)) # int
print(type(z))   # int



x = 1.10  # float
y = 1.0   # float
z = -35.59  # float

print(type(x))  # float
print(type(y))  # float
print(type(z))  # float


x = 35e3  # float
y = 12E4  # float
z = -87.7e100  # float

print(type(x)) # float
print(type(y))  # float
print(type(z)) # float



x = 3+5j  # complex
y = 5j  # complex 
z = -5j  # complex

print(type(x))  # complex
print(type(y))  # complex 
print(type(z)) # complex


x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x)
b = int(y)
c = complex(x)

print(a)  # float
print(b)  # int
print(c) # complex

print(type(a)) # float
print(type(b)) # int
print(type(c)) # complex


import random

print(random.randrange(1, 10)) #from 1 to 10 random number


