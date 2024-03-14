file = open('test.txt' , 'r')
file2 = open('test2.txt' , 'a')
file2.write(file.read())