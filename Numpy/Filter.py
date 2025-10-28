import numpy as np

nums = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

mask = nums > 5

filtered_nums = nums[mask]

print(filtered_nums)