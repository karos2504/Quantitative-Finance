import collections

# Double Linked List
linked_list = collections.deque([])

# Add item at tail
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

# Insert item at head
linked_list.appendleft(0)

# Remove item at tail
linked_list.pop()

# Remove item at head
linked_list.popleft()

# No indexes
# But similar can access the item by indexes
print(linked_list[0])
