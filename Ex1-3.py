length1 = 0
length1 = int(input('Please enter the length of an array: '))
print(length1)

arr = []

for i in range(length1):
    num = int(input('Enter a number for the arr: '))
    print(num)
    arr.insert(i, num)

print('The arr you enter is', arr)

x = 0
x = int(input('Please enter another x number: '))

for i in range(4, len(arr)):
    print(i)
    if arr[i] < 5:
        arr[i] = arr[i] + x
    elif arr[i] > 6 and i < 10:
        arr[i] = arr[i] * x
    elif arr[i] > 10:
        arr[i] = pow(arr[i], x)

print(arr)
