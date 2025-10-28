# *args (tuple)
def show_name(*name):
    for i in range(len(name)):
        print(name[i])

show_name('Karos', 'Love', 'Sia')

# **kargs (dict)
# Keyword argument - ** to represent an arbitrary number of keyword arguments
def show_info(**parameter):
    print(parameter['fname'])
    print(parameter['lname'])
    print(parameter['age'])

show_name('Karos', 'Love', 'Sia')
show_info(fname='Khoa', lname='Nguyen', age='21')

# yield
'''
    yield is a keyword that is used to turn a function into a generator
    
    return sends a single value and ends the function.
    yield sends a value, but the function doesn't end. The function will resume when the next value is requested.
'''

def producer():
    for num in range(0, 10, 1):
        if num % 2 == 0:
            yield num

for num in producer():
    print(num)
    