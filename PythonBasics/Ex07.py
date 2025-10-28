names = ['Adam', 'Daniel', 'Ana']
ages = [34, 12, 54]

my_dict = {}

for key, value in zip(names, ages):
    my_dict[key] = value

print(my_dict)
