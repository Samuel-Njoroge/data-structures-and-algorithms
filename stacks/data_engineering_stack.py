class Stack():
    # Empty stack
    def __init__(self):
        self.stack = []
    
    # Adding items in the stack
    def push(self, item):
        self.stack.append(item)
    
    # Removing items
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
    
    # Size of the stack
    def size(self):
        return len(self.stack)
    
    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    
    # Items in the stack
    def show_items(self):
        return self.stack

# Instance data engineering    
data_engineering = Stack()

# Adding items
data_engineering.push('Apache Airflow')
data_engineering.push('Apache Kafka')
data_engineering.push('Apache Spark')
data_engineering.push('Apache Hive')
data_engineering.push('Apache Beam')

# Removing items
data_engineering.pop()

# Size of the stack
print(data_engineering.size)

# Items in the stack
print(data_engineering.show_items())