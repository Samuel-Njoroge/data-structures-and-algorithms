# A queue using modules
import collections

countries_queue = collections.deque()

# Adding elements
countries_queue.append('Kenya')
countries_queue.append('Canada')
countries_queue.append('Germany')

# Removing from left
countries_queue.popleft()
print(countries_queue)

# Indexing
print(countries_queue[-1])

# Size of queue
print(countries_queue.__sizeof__())
