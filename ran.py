n = int(input("Enter a number : "))
i = 2
while n ** 0.5 >= i :
    if n % i == 0 :
        print("False")
        break
    i += 1
else :
    print("True")