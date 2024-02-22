def myfunc(n):
  return lambda a : a * n
doubler = myfunc(5)
print(myfunc(5))

