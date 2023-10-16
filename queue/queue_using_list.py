# Implementation of a queue using a list.
countries_queue = []

# Adding elements
countries_queue.append('Kenya')
countries_queue.append('Uganda')
countries_queue.append('Rwanda')
countries_queue.append('Nigeria')
countries_queue.append('Ghana')

print(countries_queue)

# Removing items
countries_queue.pop(0) # First element - Kenya
countries_queue.pop(-1) # Last element - Ghana

print(countries_queue)

# Checking if empty
print(not countries_queue)