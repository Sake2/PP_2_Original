from itertools import permutations
def print_permutations(strr):
    perm = permutations(strr)
    for p in perm:
        print(''.join(p))
strr = input("Enter a string: ")
print_permutations(strr)
