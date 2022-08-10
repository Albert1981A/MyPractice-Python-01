
arr = [{"id": 1, "name": "Ron"},
        {"id": 2, "name": "Dana"},
        {"id": 3, "name": "Avi"}]

# Get all Names from the Array
names_arr = list(map(lambda x : x["name"],arr))
print(names_arr)



