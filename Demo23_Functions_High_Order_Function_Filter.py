
arr = [{"id": 1, "name": "Ron"},
        {"id": 2, "name": "Dana"},
        {"id": 3, "name": "Avi"}]
        
print('This is arr', arr)

# Get only element that their name starts with 'D'
arr2 = list(filter(lambda x : x["name"].startswith('D') ,arr))
print('This is arr2', arr2)

# Get element by id
arr2 = list(filter(lambda x : x["id"] == 3 ,arr))
print('This is arr2', arr2)
