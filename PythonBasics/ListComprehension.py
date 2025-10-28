# List Comprehension
numbers = [1, 5, 43, 55, 76, 100, 123, 11, 2, -5, 87, 99]

def is_prime(x):
 
    if x < 0:
        return False
    if x == 1:
        return False
    if x == 2:
        return True
 
    for num in range(2, x):
        if x % num == 0:
            return False
 
    return True 

# (return, loop, condition)
list_prime = [num for num in numbers if is_prime(num)]
print(list_prime)

list_square = [num * num for num in range(5, 11)]
print(list_square)
