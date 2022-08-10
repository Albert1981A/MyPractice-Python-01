
from functools import reduce


arr = [6,2,8,12,4]

def find_min(x,y):
    if x < y:
        return x
    else:
        return y

result = reduce(lambda x,y : find_min(x,y) ,arr)
print(result)