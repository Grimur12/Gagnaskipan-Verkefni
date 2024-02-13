from array_deque import ArrayDeque
from my_linked_list import LinkedList

class Stack:
    def __init__(self):
        # Nota self.container = ArrayDeque()

        self.container = ArrayDeque()

    def push(self, data):
        # Nota push_back úr Deque
        self.container.push_back(data)
    
    def pop(self):
        # Nota pop_back úr Deque

        return self.container.pop_back()
    
    def get_size(self):
        
        return self.container.get_size()

    def __str__(self):
        return ""

# Stack er First in - First Out
# Þannig /5 /4 /3 /2 /   .append tekur aftana /5 /4 /3 /2 / 1/
# Og pop tekur það stak i burtu /5 /4 /3 /2 / 1/ verður /5 /4 /3 /2 / 
