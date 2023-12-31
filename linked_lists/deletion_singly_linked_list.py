# Deletion of a node

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
    
    # Insertion in an empty linked list
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty!")
    
    # Deletion at the beginning
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty, can't delete nodes!")
        else:
            self.head = self.head.ref

    # Deletion at the end
    def delete_end(self):
        if self.head is None:
            print("Linked list is enpty, can't delete node")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    def delete_by_value(self, x):
        if self.head is None:
            print("Can't delete, Linked List is empty")
            return
        if x ==self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n= n.ref



LL1 = LinkedList()
LL1.add_begin(20)

LL1.add_end(100)
LL1.add_end(110)

LL1.add_after(105, 100)
LL1.add_after(30, 20)

LL1.add_before(25, 30)
LL1.add_before(95, 100)

LL1.delete_begin()
LL1.print_LinkedList()

LL1.delete_end()
LL1.print_LinkedList()

LL1.delete_by_value(20)
LL1.print_LinkedList()