def solve(numheads, numlegs):
    rabbit = (numlegs -2 * numheads ) / 2
    chicken = (numheads *4 - numlegs) / 2 
    return [rabbit,chiccken]
numheads = int(input())
numberlegs = int(input())
print(solve(numheads,numberlegs))