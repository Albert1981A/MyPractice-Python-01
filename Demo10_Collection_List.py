print('--------------------------Start---------------------------')

arr = [7,2,5]
print('Initial Array', arr)

# Add item to the END of the list
arr.append(6)
print('Add item to the END of the list (append)', arr)
arr.append(8)
print('Add item to the END of the list (append)', arr)


# Add item to a specific index in the list
arr.insert(1, 10) # 1 is the index (the second place) and 10 is the element
print('Add item to a specific index (insert)', arr)


# Remove item from the end of the list
arr.pop()
print('Remove item from the end of the list (pop)', arr)


# Remove item from a specific index in the list
num = arr.pop(1)
print('Remove item from a specific index in the list (pop(index))', arr)
print('This is the item that we remove from index 1 ', num)

print('---------------------------End--------------------------')