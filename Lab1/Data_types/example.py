x = 5
print(type(x)) #<class 'int'>


x = "Hello World"
print(x)        #Hello world              
print(type(x))  #<class 'str' >


x = 20
print(x)        #20
print(type(x)) # <clas 'int'>


x = 20.5
print(x) #20.5
print(type(x))  #<class 'float'>


x = 1j
print(x) #1j
print(type(x))  #<class 'complex'>


x = ["apple", "banana", "cherry"]
print(x) #['apple', 'banana', 'cherry']
print(type(x)) #<class 'list'>


x = ("apple", "banana", "cherry")
print(x) #('apple', 'banana', 'cherry')
print(type(x)) #<class 'tuple'>


x = range(6)
print(x) #range(0, 6)
print(type(x)) #<class 'range'>


x = frozenset({"apple", "banana", "cherry"})
print(x) #frozenset({'banana', 'cherry', 'apple'})
print(type(x)) #<class 'frozenset'>


x = True
print(x) #True
print(type(x)) #<class 'bool'>


x = b"Hello"
print(x) #b'Hello'
print(type(x)) #<class 'bytes'>


x = bytearray(5)
print(x) #bytearray(b'\x00\x00\x00\x00\x00')
print(type(x)) #<class 'bytearray'>


x = memoryview(bytes(5))
print(x) #<memory at 0x000001CA6AC94C40>
print(type(x)) #<class 'memoryview'>


x = None
print(x) #None
print(type(x)) #<class 'NoneType'>




