import os

def check_aces_file(filename):
    try :
        filee = open(filename,"r")
        print ("file is exist")
        print ("file is readible")
        filee.close()
    except IOError :
        print("file is not exist")
        print ("file is no readible")
   
    try :
        filee = open(filename,"w")
        print ("file is writhtable")
        filee.close()
    except :
        print("file is not wrightable")
        
    try :
        filee = open(filename,"a")
        print ("file is executable")
        filee.close()
    except :
        print("file is not executable") 
        
filename = input()  
filename = "test.txt"
print(check_aces_file(filename))