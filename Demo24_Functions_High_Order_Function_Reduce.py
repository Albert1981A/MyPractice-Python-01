from functools import reduce
arr = [5,2,3,6]

result = reduce(lambda x,y : x + y, arr) # reduce always receives 2 parameters
print('result is:', result) # Will print 16

# the way reduce works:
# x + y => 5 + 2 => 7
#          x + y => 7 + 3 => 10
#                   x + y => 10 + 6 => 16 