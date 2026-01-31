from functools import reduce
L = [111, 2, 65, 5553, 635, 65, 74, 45,55]


def greater(a, b):
    if (a>b):
        return a 
    return b

print(reduce(greater, L))