#1
import datetime
x = datetime.datetime.now()
print(x)
#2
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
#3
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)

#4
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))