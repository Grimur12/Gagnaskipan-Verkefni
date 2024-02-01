class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        # TODO: remove 'pass' and implement functionality
        self.size = 0
        self.capacity = 4
        self.arr = [None] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        # TODO: remove 'pass' and implement functionality
        return_string = ""
        for i in range(self.size):
            return_string += str(self.arr[i]) + ", "
        return_string += str(self.arr[self.size])
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # TODO: remove 'pass' and implement functionality
        self.insert(value, 0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        # TODO: remove 'pass' and implement functionality
        # Inserts an item into the list at a specific location, not overwriting other items
        # If the index is not within the current list, raise IndexOutOfBounds()
        # It should be possible to add to the front and back of the list, and anywhere in between
        self.resize()
        if index < 0 or index > self.size:
            raise IndexOutOfBounds()
        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i-1]
        self.arr[index] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def append(self, value):
        # TODO: remove 'pass' and implement functionality
        if self.size + 1 > self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        if index < 0 or index > self.size:
            raise IndexOutOfBounds()
        self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        if self.size == 0:
            raise Empty()
        return self.arr[0]


    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        if index < 0 or index > self.size:
            raise IndexOutOfBounds()
        return self.arr[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        if self.size == 0:
            raise Empty()
        return self.arr[self.size - 1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        # TODO: remove 'pass' and implement functionality
        # Re-allocates memory for a larger array and populates it with the original array’s items
        if self.size == self.capacity:
            self.capacity = self.capacity * 2
            new_arr = [None] * self.capacity
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
        

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        if index < 0 or index > self.size:
            raise IndexOutOfBounds()
        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i+1]
        self.size = self.size - 1

    #Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        # Removes all items from the list
        self.size = 0

    def check_ordered(self):
        for i in range(self.size-1):
            if self.arr[i] > self.arr[i+1]:
                return False
        return True
                
    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        if not self.check_ordered():
            raise NotOrdered()
        
        for i in range(self.size):
            if self.arr[i] > value:
                self.insert(value, i)
                return
        self.append(value)
            


    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        # ○ Returns the index of a specific value
        # ○ If the instance of ArrayList is in an ordered state, use recursive binary search
        # ○ If the ArrayList instance is not ordered, use linear search
        # ○ If the value is not found in the list, raise NotFound()
        if self.check_ordered():
            return self.binary_search(value, 0, self.size - 1)
        else:
            return self.linear_search(value)
        
    def binary_search(self, value, low, high):
        if high < low:
            raise NotFound()
        mid = (low + high) // 2
        if self.arr[mid] > value:
            return self.binary_search(value, low, mid - 1)
        elif self.arr[mid] < value:
            return self.binary_search(value, mid + 1, high)
        else:
            return mid
        
    def linear_search(self, value):
        for i in range(self.size):
            if self.arr[i] == value:
                return i
        raise NotFound()
        
        

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        # ○ Removes from the list an item with a specific value
        # ■ Can you use only helper functions that have already been implemented?
        # ○ If the value is not found in the list, raise NotFound
        index = self.find(value)
        self.remove_at(index)


if __name__ == "__main__":
    my_list = ArrayList()

    # til að appenda value
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)
    my_list.append(6)
    my_list.append(7)
    my_list.append(8)
    my_list.append(9)
    my_list.append(10)
    
    print(my_list)
    print("=" * 50)

     # fyrir value
    try:
        index = my_list.linear_search(10)
        print(f"{index}")
    except NotFound:
        print("Value not found")

    # til að inserta value á akveðna index
    my_list.insert(4, 1)  

    # til að fjarlægja value á akveðna index
    my_list.remove_at(2)  # Removes value at index 2

    print(my_list)

    print("=" * 50)

    my_list.clear()
    print(my_list, "Cleared")

    print( "=" * 50)

    # til að finna index á value
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(6)
    my_list.insert_ordered(5)
    print(my_list)
    print(my_list.find(4))
