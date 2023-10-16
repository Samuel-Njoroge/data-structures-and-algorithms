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