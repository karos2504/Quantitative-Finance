# Natural ordering
nums = [10, 2, 4, 5, -9, 7, -4, -3, 1]

# Sorted function always return a list
# Desending order - reverse
result = sorted(nums, reverse=True)
print(result)

# Sorted function has the KEY parameter
def sorted_by_len(n):
    return len(n)

string = ['A', 'BC', 'DEF', 'GHKL']
result = sorted(string, key=sorted_by_len, reverse=True)
print(result)