
from functools import reduce

arr = ["Yoav", "Ron", "Aviva", "Ronen", "Dan", "Galit"]

def get_length(array):
    big_names = list(filter(lambda x : len(x) > 4 , array))
    big_names_len = list(map(lambda x : len(x), big_names))
    return reduce(lambda x , y : x + y, big_names_len)

print(get_length(arr))