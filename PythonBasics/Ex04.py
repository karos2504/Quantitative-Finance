def activation(x):
    if x < 0:
        return 0, False
    else:
        return 1, True

result = activation(23) # Tuple
print(type(result))
print(result[0])
print(result[1])
