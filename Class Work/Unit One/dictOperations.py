my_dict = {'name':'Alice', 'age':'25'}
my_dict['age'] = 26
my_dict['city'] = 'New York'
print(my_dict)
my_dict.pop('name')
print(my_dict)

for key, value in my_dict.items():
    print(f"{key}: {value}")