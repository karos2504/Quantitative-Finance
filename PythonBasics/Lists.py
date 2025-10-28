# Measuring running time of lists
import time
 
nums = []
 
# start time in seconds - we will measure the running time of operations
start = time.time()
 
# let's insert 100k items at the end of the list - fast operation
for i in range(100000):
    nums.append(i)
 
print('Inserting at the end - time taken: %s' % (time.time() - start))
 
# re-initialize time
start = time.time()
 
# insert 100k items at the beginning of the list - index 0
for i in range(100000):
    nums.insert(0, i)
 
# takes a lot of time because we have to shift the items !!!
print('Inserting at the beginning - time taken: %s' % (time.time() - start))
