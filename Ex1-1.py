arr = [17,1,12,54,23,9,21]

arr2 = []
for i in arr:
    if i > 3 and i < 20:
        print(i)
        arr2.append(i)

print('-------------------------')

print(arr2)
print(sum(arr2))
