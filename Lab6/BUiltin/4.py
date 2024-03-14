import time
def sqrt_after_time(num):
    return num  ** 0.5
def invoke_square_root_after_milliseconds(timee, number):
    time.sleep(timee / 1000)
    result = sqrt_after_time(number)
    return result
num = int(input())
timee = int(input())
print("square root of " , num ," after ", timee, " is " , invoke_square_root_after_milliseconds(timee,num))
