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
            self.rezise()
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

    #Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        # Removes all items from the list
        self.size = 0

    def binary_search(self, value):
        if self.arr == "":
            return False
        else:
            mid = self.arr // 2
            if self.arr[mid] == value:
                return True
            elif self.arr[mid] > value:
                
        

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        if ArrayList.is_ordered(self) == False:
            raise NotOrdered()
        self.insert(value, self.size)


    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level
  
  
    arr_lis = ArrayList()
    arr_lis.insert(3,0)
    arr_lis.append(4)
    arr_lis.prepend(6)
    arr_lis.insert(9,2)
    arr_lis.set_at(1, 2)
    print(str(arr_lis))
    print(arr_lis.get_first())
    print(arr_lis.get_last())
    print(arr_lis.get_at(2))
    print(arr_lis)
    arr_lis.remove_at(2)
    print(arr_lis)
    arr_lis.append(3)
    print(arr_lis)
    arr_lis.insert("Value",2)
    print(arr_lis)
    arr_lis.clear()
    print(arr_lis, "Cleared")


