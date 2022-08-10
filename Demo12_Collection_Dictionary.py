# Dictionary is build from elements that have keys and Values
# Dictionary is like a JSON
col = { 1: "Avi", 5: "Dana", 7: "Gil", "AA": 100}
print(col)

# To receive a specific value we call him by the "key"
print(col[5]) # will print "Dana" that her key is 5
print(col["AA"]) # will print "100" that his key is "AA"

# Replace a value with a new one
col[1] = "Aviva"
print('We replace "Avi" with "Aviva": ')
print(col)

# Add new key/value pair
# we need to enter new key that doesn't exist in the collection
col[12] = "Eva"
print(col)

# Get all keys:
keys = list(col.keys()) # Return a list of keys
print('List of the Keys', keys)

# How to check if a key exist in the list option 1:
if 6 in keys:
    print('Exist')
else:
    print('Don\'t Exist')

# How to check if a key exist in the list option 2:
if 6 not in keys:
    print('Don\'t Exist')
else:
    print('Exist')

# Get all Values:
values = list(col.values()) # Return a list of values
print('List of the values', values)

# Deleting a key/value pair:
del col[12]
print('We delete 12: "Eva" ', col)
