import os
try :
    path = input()
    print(os.remove(path))
except FileNotFoundError:
    print("path is not found")