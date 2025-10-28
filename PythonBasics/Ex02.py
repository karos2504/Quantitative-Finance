item_counter = 0
sum = 0
 
for item in range(1, 11):
    sum += item
    item_counter += 1
 
print('Average of the first 10 items (starting with 1) is: ' + str(sum/item_counter))