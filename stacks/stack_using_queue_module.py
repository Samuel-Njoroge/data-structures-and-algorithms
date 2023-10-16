# Stack using queue module
import queue

odd_numbers_stack = queue.LifoQueue(5) # 5 - Maximum size of the stack

# Adding items
print(odd_numbers_stack.put(1))
print(odd_numbers_stack.put(3))
print(odd_numbers_stack.put(5))
print(odd_numbers_stack.put(7))
print(odd_numbers_stack.put(9))

# Removing items
print(odd_numbers_stack.get()) # 9
print(odd_numbers_stack.get()) # 7
