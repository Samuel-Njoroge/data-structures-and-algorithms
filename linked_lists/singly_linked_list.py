"""
A linear data structure made of linked nodes
A node has the data field and the link field (which links the next node)
Last node has a link to NULL
Node - Elements in a linked list
Head - First node / starting point
Tail - End of a list
Size is not fixed / dynamic data structure
Unodered 

Examples of linked list
1. Relay running

Singly linked list

Nodes have a data as well as next field
Operations [Insertion, deletion, traversal]
The elements are not stored in contiguous memory locations
Each element is connected only to its next element using a pointer.
"""

# Insertion / Adding elements
"""
At the beginning
1. Create node
2. Change new node next = head
3. Head = the new created node

At the end
1. Create node
2. Go to last node change link of last node to new node
3. Reference of last node = the new created node

In between
1. Create a node
2. Go to node just before required position
3. Link the previous node to new node and new node to the next
"""

# Deletion
"""
At the beginning
1. Change the head of first node to the second node

At the end
1. Go to second last node, change the link to NULL

In between
2. Go to previous node
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LinkedList(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
LL1 = LinkedList()
LL1.print_LinkedList()