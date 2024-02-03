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
        self.size = 0
        self.capacity = 4
        self.arr = [None] * self.capacity
        
    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        ret_str = ""
        for i in range(self.size):
            if i != self.size-1:
                ret_str = ret_str + str(self.arr[i]) + ", "
            else:
                ret_str = ret_str + str(self.arr[i])
        return ret_str

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):

        self.insert(value,0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if index < 0 or index > self.size:
            raise IndexOutOfBounds()

        if self.size == self.capacity:
            self.resize()
            
        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i-1]
        
        self.arr[index] = value

        self.size += 1

    #Time complexity: O(1) - constant time
    def append(self, value):

        self.insert(value,self.size)

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index < 0 or index >= self.size:
            raise IndexOutOfBounds()

        self.arr[index] = value


    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty()
        return self.arr[0]
    

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexOutOfBounds()
        
        return self.arr[index]
    

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.size == 0:
            raise Empty()
        return self.arr[self.size-1]
        

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr


    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise IndexOutOfBounds()

        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i+1]
        
        self.size -= 1

    #Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0
        self.arr = [None]*self.capacity

    def Linear_Search(self, array, value, index = 0):
        if array:
            if array[0] == value:
                return index
            checker = self.Linear_Search(array[1:],value, (index + 1))
            if checker is not False:
                return checker
    
        return False

    def Binary_search(self, array, value, size, index = 0):
        if size <= 0:
            return False
        
        mid = size // 2
        if array[mid] == value:
            return index + mid
        elif value > array[mid]:
            return self.Binary_search(array[mid + 1 :], value, size - mid - 1, index + mid + 1)
        elif value < array[mid]:
            return self.Binary_search(array[:mid], value, mid, index)
        else:
            return False

    def check_ordered(self):
        for i in range(self.size-1):
            if self.arr[i] > self.arr[i+1]:
                return False
        return True
            
    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        if not self.check_ordered():
            raise NotOrdered()

        for i in range(self.size):
            if self.arr[i] > value:
                self.insert(value,i)
                break
        else:
            self.append(value)

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        if self.check_ordered():
            binary_index = self.Binary_search(self.arr, value, self.size)
            if binary_index is not False:
                return binary_index
            else:
                raise NotFound()
        else:
            linear_index = self.Linear_Search(self.arr,value)
            if linear_index is not False:
                return linear_index  
            else:
                raise NotFound()

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):

        index = self.find(value)
        
        return self.remove_at(index)


if __name__ == "__main__":
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level
    pass