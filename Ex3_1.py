
from functools import reduce


def string_length(string):
    return len(string)

print(string_length('Barbara'))

arr = ["Bamba", "Bisley", "Chips"]

def total_length(array):
    list_of_length = list(map(lambda x :  string_length(x), array))
    return reduce(lambda x,y : x+y, list_of_length)

print(total_length(arr))
