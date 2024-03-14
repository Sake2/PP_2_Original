import os 
 
path = input()
#path = "C:\\Users\\Аяулым\\Desktop\\PP_2"
os.chdir(path)
print(os.listdir(path))