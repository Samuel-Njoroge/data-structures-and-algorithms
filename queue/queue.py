"""
A linear data structure that is open at  both ends
front / head - Entry position / first
rear / tail - Last position / Most recently added
FIFO - First In First Out
LILO - Last In Last Out 
enqueue() - Add elements 
degueue() - Remove elements

Characteristics of queues
1. Can handle multiple data
2. We can access both ends
3. Fast and flexible

Applications of queues
1. Call centres
2. 
"""

# Adding and removing elements in a queue
queue = []
def enqueue():
    element = input("Enter the element: ")
    queue.append(element)
    print(element, "added to the queue")

def dequeue():
    if not queue:
        print("Queue is empty!")
    else:
        e = queue.pop(0)
        print("Removed element: ", e)

def display():
    print(queue)

while True:
    print("Select the operation 1. add 2. remove 3. show 4. quit")
    choice = int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Incorrect choice!")
