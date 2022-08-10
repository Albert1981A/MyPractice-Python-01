def add(num1,num2):
    if num1+num2 > 10:
        print(num1+num2)
    else:
        return num1+num2


total = add(3,4)
print("returned Value " + str(total)) # will print: "returned Value 7"

total = add(6,9) # will print from the function: "15"
print("returned Value " + str(total)) # will print: "returned Value None"

