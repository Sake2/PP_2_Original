class  To_string :
    def __init__(self) :
        self.str = ""
    def getstring(self):
        self.str = input()
    def printstring(self):
        print(self.str.upper())

x = To_string()
x.getstring()
x.printstring()
