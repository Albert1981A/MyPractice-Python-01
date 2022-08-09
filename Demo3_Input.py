name = input('Enter Name: ')
print(name)

age = input('Enter Age: ')
print(age*2) # if we enter 20 this will print 2020. this is because it receives the 20 es a string


age2 = input('Enter Age: ')
print(int(age2)*2) # we need to convert the received number from string to Integer to multiply it

print('Hello', name+ ', your age is', str(age2)) # we need to convert integer to string to print it

# 40:18