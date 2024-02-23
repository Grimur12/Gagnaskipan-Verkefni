
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current_position = 0
        # [ -1 , 0, 1, 2, 3, self.size = 4 ]
        # [HEAD, 1, 2, 3, 4, TAIL]
        self.current_node = self.tail
        self.size = 0

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.current_node
        new_node.prev = self.current_node.prev
        self.current_node.prev.next = new_node
        self.current_node.prev = new_node
        self.current_node = new_node
        self.size += 1
        self.current_position += 1

    def remove(self):
        if self.current_node.next:
            self.current_node.prev.next = self.current_node.next
            self.current_node.next.prev = self.current_node.prev
            self.current_node = self.current_node.next
            self.current_position -= 1
            self.size -= 1
        # Þetta þarf að laga
        # if self.size == 0:
        #     return
        # if self.current_node.next:
        #     self.current_node.prev.next = self.current_node.next
        #     self.current_node.next.prev = self.current_node.prev
        #     self.current_node = self.current_node.next
        #     self.current_position -= 1
        # else:
        #      self.current_node = self.current_node.prev
        #      self.current_node.prev.next = self.current_node.next
        #      self.current_node.next.prev = self.current_node.prev
        #      self.current_node = self.current_node.next
        #      self.current_position += 1
        # self.size -= 1

    def get_value(self):
        return self.current_node.data       

    def move_to_next(self):
        if self.current_node == self.tail: # Testcase virkar ef ég leyfi move_to_next að fara á self.tail
            return
        else:
            self.current_node = self.current_node.next
            self.current_position -=1

    def move_to_prev(self):
        if self.current_node.prev == self.head:
            return
        else:
            self.current_node = self.current_node.prev
            self.current_position +=1

    def move_to_pos(self, pos):
        # Það þarf að breyta þessu aðeins, gera flottara
        if pos > self.size or pos <= -1:
            return
        current_pos = 0
        curr_node = self.head
        while curr_node and current_pos < pos:
            curr_node = curr_node.next
            current_pos += 1
        self.current_position = self.size - current_pos
        self.current_node = curr_node.next
        

    def clear(self):
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current_position = 0
        self.current_node = self.tail
        self.size = 0

    def get_first_node(self):
        return self.head.next

    def get_last_node(self):
        return self.tail.prev

    def partition(self, low, high):

        pivot = low.data # Til að bera saman stökin 
        # Viljum byrja að loopa yfir listann með næsta staki til að bera saman
        curr_node = low.next
        # Þegar curr_node hitir high þá er partition búið
        while curr_node != high.next and curr_node.data: # Þarf að hafa curr_node.data má ekki vera None líka

            next_node = curr_node.next # Þurfum að geyma fyrir iteration aður en við byrjum að swappa öllu

            if curr_node.data < pivot:
                # Tengja framhjá current node sem er minni 
                curr_node.prev.next = curr_node.next 
                curr_node.next.prev = curr_node.prev 
                # Tengja curr_node við það sem var áður fyrir framan low
                curr_node.prev = low.prev
                low.prev.next = curr_node
                # Tengja low við þann stað sem curr_node var áður
                low.prev = curr_node
                curr_node.next = low

            curr_node = next_node

        # Benda á partition pivotinn
        self.current_node = low
    
    def swap_data(self, curr, next):
        temp_data = curr.data
        curr.data = next.data
        next.data = temp_data

    def sort(self):
        # Virkar en er ekki quick sort
        first = self.get_first_node()
        last = self.get_last_node()
        
        curr_node = first

        while curr_node != last.next and curr_node.data:

            next_node = curr_node.next

            while next_node != last.next and next_node.data:
                if curr_node.data > next_node.data:
                    self.swap_data(curr_node, next_node)

                next_node = next_node.next
            
            curr_node = curr_node.next

        self.current_node = self.head.next


    def quicksort(low, high):
        pass

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        curr_node = self.head.next
        while curr_node != self.tail:
            ret_str += str(curr_node.data) + " "
            curr_node = curr_node.next
        return ret_str

if __name__ == "__main__":
    dll = DLL()
    dll.insert(1)
    dll.insert(3)
    dll.insert(4)
    dll.insert(2)
    dll.insert(7)
    dll.insert(6)
    dll.insert(5)
    dll.insert(10)
    dll.insert(8)
    dll.insert(9)
    dll.insert(12)
    dll.insert(11)
    dll.insert(15)
    dll.insert(13)
    dll.insert(14)
    dll.insert(16)
    print(dll)
    print(dll.get_first_node().data)
    print(dll.get_last_node().data)
    dll.partition(dll.get_first_node(),dll.get_last_node())
    print(dll)
    dll.sort()
    print(dll)
    # dll = DLL()
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # dll.insert("A")
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # dll.insert("B1")
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # dll.insert("C")
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # dll.insert("A")
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # dll.insert("B2")
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))
    # dll.partition(dll.get_first_node(), dll.get_last_node())
    # print(str(dll) + "   -   current value: " + str(dll.get_value()) + "   -   size: " + str(len(dll)))


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        