# Adding elements at the beginning of the list
"""
1. Create a new node
2. New node = head
3. head = new_node
"""

# Insertion of elements in the node
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
    # Insertion at the beginning of the node
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # Insertion at the end of the node
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    # Insertion between the nodes (after a node)
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x==n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    # Insertion between nodes (before a node)
    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is empty!")
            return
        
        if self.head ==x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n = n.ref

        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


LL1 = LinkedList()
LL1.add_begin(20)

LL1.add_end(100)
LL1.add_end(110)

LL1.add_after(105, 100)
LL1.add_after(30, 20)

LL1.add_before(25, 30)
LL1.add_before(95, 100)

LL1.print_LinkedList()