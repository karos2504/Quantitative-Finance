import numpy as np

nums = np.array([1, 2, 3, 4, 5, 6])
nums = nums.reshape(2, 3)
print(nums)

# Use -1 "unknow" dimension
nums = nums.reshape(6, -1)
print(nums)