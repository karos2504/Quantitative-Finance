class Person:
    # Private variable
    _name = 'Karos'

    # Name mangling
    __age = 21

p = Person()
# print(p._name)
print(p._Person__age)