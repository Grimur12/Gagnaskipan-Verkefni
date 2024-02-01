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
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # TODO: remove 'pass' and implement functionality
        self.insert(value, 0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        # TODO: remove 'pass' and implement functionality
        pass

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
        pass

    #Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        pass

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
        pass

    #Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

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
    print(str(arr_lis))