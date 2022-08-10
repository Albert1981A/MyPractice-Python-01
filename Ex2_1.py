arr = []
num = 0

while num <= 10:
    num = int(input('Enter new Number: '))
    if num not in arr:
        arr.append(num)
    else:
        print('Number already exist')

print(arr)

# for i in range(len(arr)):
#     print('len:', len(arr))
#     num = arr.pop()
#     print(num)

while len(arr) > 0:
    num = arr.pop()
    print(num)

print(arr)
