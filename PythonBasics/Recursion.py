# Recursion
def sum_iterator(n):
    if n == 0:
        return 0
    return n + sum_iterator(n - 1)

print(sum_iterator(10))
