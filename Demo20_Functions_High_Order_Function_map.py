
arr = [6,3,8,1,7]
print('This is arr', arr)

# if we want to multiply every element in 2
# there is two ways to do it 

# Option-1:
arr2 = []
for ptr in arr:
    arr2.append(ptr * 2)

print('This is arr2', arr2)

# Option-2:
# Using "map" ( map() ) => the first element that the map receives its a lambda function, the second is the array we run on
# the map function return a "map Object" we receives the content of the map Object with List function ( list() )
# The List Function return an array
arr3 = list(map(lambda x : x*2, arr))
print('This is arr3', arr3)