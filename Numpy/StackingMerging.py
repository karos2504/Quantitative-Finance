import numpy as np 

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

# Vertical stacking
vertical = np.vstack((a, b))
print(f'Vertical stacking: {vertical}')

# Horizon stacking
horizon = np.hstack((a, b))
print(f'Horizon stacking: {horizon}')

# Stack
result = np.stack((a, b), axis=0)
print(f'Axis 0: {result}')

result = np.stack((a, b), axis=1)
print(f'Axis 1: {result}')