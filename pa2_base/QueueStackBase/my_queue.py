from array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    def __init__(self):
        # Nota self.container = LinkedList()
        self.container = LinkedList()

    def add(self, data):
        # Push_back
        return self.container.push_back(data)
    
    def remove(self):
        # Pop_front
        return self.container.pop_front()

    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return ""

# Queue er last in first out þannig push_back til að appenda og síðan pop_front() til að taka framaná