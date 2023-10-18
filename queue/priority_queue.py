# Priority queue using a list
odd_numbers_queue = []

odd_numbers_queue.append(1)
odd_numbers_queue.append(5)
odd_numbers_queue.append(3)

odd_numbers_queue.sort()
print(odd_numbers_queue)


# Priority queue using 
import queue

even_numbers_queue = queue.PriorityQueue()

even_numbers_queue.put(2)
even_numbers_queue.put(8)
even_numbers_queue.put(6)
even_numbers_queue.put(4)

print(even_numbers_queue)

# Removing items
even_numbers_queue.get()