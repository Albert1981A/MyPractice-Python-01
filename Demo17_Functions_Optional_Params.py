def add(num1 = 10, num2 = 9, num3 = 4):
    print(num1 + num2 + num3)

add()        # will use the default numbers
add(7)       # 7 will change num1, num2 and num3 will use the default
add(7, 5)    # 7 will change num1, 5 will change num2 and num3 will use the default
add(7, 5, 8) # 7 will change num1, 5 will change num2 and 8 will change num3 