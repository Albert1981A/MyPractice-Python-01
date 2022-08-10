
lambda x : x*2  
#  This is an anonymous function.
#  It's a function with no name.
#  It dose have an address in the memory.

f1 = lambda x : x * 2
#  f1 is a pointer in the stuck to the function in the heap.

res = f1(4)
print(res) 
#  with the pointer f1 we can call the function.


f2 = lambda x,y,z : x+y+z
res2 = f2(5, 6, 4)
print(res2)
# function that receives parameter and do some thing with them


f3 = lambda : print("Hello")
f3()
# function that don't receives any parameter and do some thing
