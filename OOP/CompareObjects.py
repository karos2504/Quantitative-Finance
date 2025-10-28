class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __gt__(self, other):
        return self.age > other.age

p1 = Person('Karos', 21)
p2 = Person('Khoa', 23)

print(p1 == p2)
print(p1 < p2)
print(p1 > p2)
