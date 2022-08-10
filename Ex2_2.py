students = {1: [50,70,90,70], 2: [60,90,80], 3: [90,100] }

key = int(input('Enter student id: '))

while key > 0:
    if key in list(students.keys()):
        print('the heist grade of student id', str(key), 'is', str(max(students[key])))
        break
    else:
        print('number dont Exist')
        key = int(input('Enter student id: '))

print('END')