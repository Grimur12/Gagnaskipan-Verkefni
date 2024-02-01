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
        # Bara til að byrja með til að geta testað allt dótið, ég held að þetta megi ekki
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

        ## Virkar        

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if self.size == self.capacity:
            self.resize()
            
        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i-1]
        
        self.arr[index] = value

        self.size += 1

        ## Virkar

    #Time complexity: O(1) - constant time
    def append(self, value):
  
        self.insert(value,self.size)

        ## Virkar

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index < 0 or index > self.size:
            raise IndexOutOfBounds()

        self.arr[index] = value

        ## Virkar

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.size == 0:
            raise Empty()
        return self.arr[0]
    
        ## Virkar

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if index < 0 or index > self.size:
            raise IndexOutOfBounds()
        
        return self.arr[index]
    
        ## Virkar

    #Time complexity: O(1) - constant time
    def get_last(self):

        return self.arr[-1]
        
        ## Virkar

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

        ## Virkar

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if index < 0 or index > self.size:
            raise IndexOutOfBounds()

        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i+1]
        
        self.size -= 1

        ## Virkar


    #Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0
        

    def Linear_Search(self, array, value, index = 0):
        if array:
            if array[0] == value:
                return index
            checker = self.Linear_Search(array[1:],value, (index + 1))
            if checker is not False:
                return checker
    
        return False

        ## Virkar

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

        ## Virkar

    def check_ordered(self):
        for i in range(self.size-1):
            if self.arr[i] > self.arr[i+1]:
                return False
        return True
    
        ## Virkar
            

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        if not self.check_ordered():
            raise NotOrdered()

        for i in range(self.size):
            if self.arr[i] > value:
                self.insert(value,i)
        
        ## Virkar


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

    arr_lis = ArrayList()
    arr_lis.insert(3,0)
    arr_lis.append(4)
    arr_lis.prepend(6)
    arr_lis.insert(9,2)
    arr_lis.set_at(5,3)
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
    print(arr_lis.find(3))
    arr_lis.clear()
    print(arr_lis, "Cleared")
    arr_lis.append(1)
    arr_lis.append(2)
    arr_lis.append(3)
    arr_lis.append(4)
    arr_lis.append(6)
    arr_lis.append(7)
    arr_lis.append(8)
    arr_lis.append(9)
    arr_lis.append(10)
    arr_lis.append(11)
    arr_lis.insert_ordered(5)
    print(arr_lis)
    print(arr_lis.find(3))
    arr_lis.remove_value(8)
    print(arr_lis)
