# A stack using collections module
import collections

even_numbers_stack = collections.deque()
even_numbers_stack

# Adding elements
even_numbers_stack.append(2)
even_numbers_stack.append(4)
even_numbers_stack.append(6)
even_numbers_stack.append(8)
even_numbers_stack.append(10)

print(even_numbers_stack)

# Removing elements
even_numbers_stack.pop() # 10
even_numbers_stack.pop() # 8

print(even_numbers_stack)

# Checking if stack is empty
print(not even_numbers_stack) # False if stack is not empty
print(len(even_numbers_stack))

# Indexing in a stack
print(even_numbers_stack[0]) # First element
print(even_numbers_stack[1]) # Second element