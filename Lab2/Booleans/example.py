print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False


a = 15
b = 9
if a > b:
    print("b is less than a")
else :
    print ("b is greater than a or equal")


print(bool("HEllO")) #True
print(bool(1))#True

x = "HELLLO" 
y = 234
print(bool(x))#True
print(bool(y))#True

bool("ghj") #True
bool(234) #True
bool(["car",2]) #True

bool(False) #False
bool(None) #False
bool(0) #False
bool("") #False
bool(()) #False
bool([]) #False
bool({}) #False


class myclass():
  def __len__(self):
    return 0  
myobj = myclass()
print(bool(myobj))


def myFunction() :
  return True
print(myFunction())


def myFunction1() :
  return True
if myFunction1():
  print("YES!")
else:
  print("NO!")


  x = 200
print(isinstance(x, int))

