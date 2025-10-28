# Set is implementd with the help of a dictionary - it use arrays under the hood
# Sets are unordered, un-indexed and non duplicated
my_set = {'Karos', 21, '5ft7', True}

# Add
my_set.add(1)

# Update
my_set.update([2, 3])

# Remove (raise Error if not found)
my_set.remove(123)

# Dicard (not raise Error)
my_set.discard(123)

# Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)