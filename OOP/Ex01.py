class Car:
    # Class variable
    color = 'black'

    # Instance variables
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_brand(self):
        return self.brand
 
    def get_year(self):
        return self.year
    
    def __str__(self):
        return f'{self.brand, self.year}'

c = Car('BMW', 2025)
print(c.__str__())