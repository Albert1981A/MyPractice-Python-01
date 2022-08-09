# Print the maximum total among the arrays
arr = [ [32,15] , [1,7,12] , [8,14,6,11] ]

total = 0 
sum1 = 0
for i in arr:
    sum1 = sum(i)
    print('sum1 is:', sum1)
    if total < sum1:
        total = sum1

print('total is', total)