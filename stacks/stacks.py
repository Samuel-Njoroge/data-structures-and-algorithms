"""
User defined data structure that follow the LIFO (Last In First Out) or First In Last Out (FILO) principle.
Ordered items
Examples of stacks in real life include:
1. A stack of books
2. A stack of plates
3. A stack of pancakes
4. A stack of coins
5. A stack of chairs
"""

# Creating a stack using a list
my_stack = []

# Adding items using the append() method
my_stack.append('Sam')
my_stack.append('Kin')
my_stack.append('Data Scientist')

print(my_stack)

# Removing elements using pop() method - removes the last element
my_stack.pop()
print(my_stack)

# Length of the stack
print(len(my_stack))

