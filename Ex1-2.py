num = 0
total = 0

while num < 10:
    num = int(input('Enter num: '))
    total += num
    if total > 30:
        print(total)
        break

print('End')