a = "Hello"
print(a)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


b = "Hello, World!"
print(b[2:5])


b = "Hello, World!"
print(b[:5]) #Hello


a = "Hello, World!"
print(a.upper()) #HELLO , WORLD


a = "Hello, World!"
print(a.lower()) #hello,world


a = " Hello, World! "
print(a.strip()) # "Hello, World!"


a = "Hello, World!"
print(a.replace("H", "J")) #Jello, world


a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


a = "Hello"
b = "World"
c = a + b
print(c) #HelloWorld


a = "Hello"
b = "World"
c = a + " " + b
print(c) #Hello World


"""age = 36
txt = "My name is John, I am " + age
print(txt)"""


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) #My name is John, and I am 36


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) #I want 3 pieces of item 567 for 49.95 dollars.


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) #I want to pay 49.95 dollars for 3 pieces of item 567.


"""txt = "We are the so-called "Vikings" from the north." """


txt = "We are the so-called \"Vikings\" from the north."








