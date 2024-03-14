import os
try :
    path = input()
    os.chdir(path)
    print(os.listdir())
except FileNotFoundError:
    print("path is not found")