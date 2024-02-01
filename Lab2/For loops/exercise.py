#1
for x in [0, 1, 2]:
  pass

#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#3
for x in range(6):
    print(x)

#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)