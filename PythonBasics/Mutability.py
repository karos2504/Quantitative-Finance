# immutable objects - number, floating points, booleans, tuples
x = 5
print(id(x))

x += 1
print(id(x))

# mutable object - lists, sets, dicts
my_list = [1, 2, 3, 4, 5]
print(id(my_list))

my_list.append(6)
print(id(my_list))
