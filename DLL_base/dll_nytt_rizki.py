class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.size = 0
        self.head = Node('Head')
        self.tail = Node('Tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr = self.tail
        self.curr_pos = -1

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.curr
        new_node.prev = self.curr.prev
        self.curr.prev.next = new_node
        self.curr.prev = new_node
        self.curr = new_node
        self.curr_pos += 1
        self.size += 1


    def remove(self):
        if self.size != 0 and self.curr_pos != -1:
            self.curr = self.curr.next
            self.curr.prev.prev.next = self.curr
            self.curr.prev = self.curr.prev.prev
            self.size -= 1
            self.curr_pos -= 1


    def get_value(self):
        if self.size != 0:
            if self.curr == self.tail:
                return None
            else:
                return self.curr.data
        

    def move_to_next(self):
        if self.curr_pos != -1:
            self.curr = self.curr.next
            self.curr_pos -= 1
        
    def move_to_prev(self):
        if self.curr_pos != self.size-1:
            temp = self.curr.prev
            self.curr = temp
            self.curr_pos += 1

    def move_to_pos(self, pos):
        if pos >= 0 and pos < self.size:
            temp_node = self.head
            for i in range(pos+1):
                temp_node = temp_node.next
            self.curr_pos = self.size-1 - pos
            self.curr = temp_node

    def clear(self):
        self.__init__()

    def get_first_node(self):
        if self.size != 0:
            return self.head.next


    def get_last_node(self):
        if self.size != 0:
            return self.tail.prev


    def partition(self, low, high):
        pivot = low
        while pivot != self.tail:
            if pivot.data < low.data:
                temp = pivot
                pivot.prev.next = pivot.next
                pivot.next.prev = pivot.prev
                temp.prev = low.prev
                temp.next = low
                low.prev.next = temp
                low.prev = temp
            pivot = pivot.next
        self.curr = low
        return high
    
    def quickSort(self, low, high):
        if low != high and low.prev != high:
            pivot = self.partition(low, high)
            self.quickSort(low, pivot.prev)
            self.quickSort(pivot.next, high)


    def sort(self, low = None, high = None):
        if low == None and high == None:
            low = self.get_first_node()
            high = self.get_last_node()
            self.quickSort(low, high)

        
    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        temp_node = self.head.next
        for low in range(self.size):
            ret_str += str(temp_node.data) + ' '
            temp_node = temp_node.next
        return ret_str


if __name__ == "__main__":
    #create tests here if you want
    a = DLL()
    a.insert(13)
    a.insert(8)
    a.insert(1)
    a.insert(2)
    a.insert(8)
    a.insert(11)
    a.insert(7)
    a.insert(13)
    a.insert(4)
    a.insert(2)
    a.insert(8)
    a.insert(1)
    a.insert(15)
    a.insert(10)
    a.insert(14)
    a.insert(7)
    a.insert(7)
    a.insert(10)
   
    print(a)
    a.partition(a.get_first_node(),a.get_last_node())
    print(a)
    a.sort()
    print(a)
    
    a.move_to_pos(0)
    print(a.get_value())
    a.move_to_next()
    print(a.get_value())
    a.move_to_next()
    print(a.get_value())
    a.move_to_next()
    print(a.get_value())


    
   