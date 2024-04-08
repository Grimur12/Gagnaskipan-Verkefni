class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Bucket: 
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, key, data):
        if self.contains(key):
            raise ItemExistsException()
        self.head = Node((key, data), self.head)
        self.size += 1

    def update(self, key, data):
        current = self.head
        while current != None:
            if current.data[0] == key:
                current.data = (key, data)
                return
            current = current.next
        else:
            raise NotFoundException()
    
    def find(self, key):
        current = self.head
        while current != None:
            if current.data[0] == key:
                return current.data[1]
            current = current.next
        else:
            raise NotFoundException()
        
    def contains(self, key):
        current = self.head
        while current != None:
            if current.data[0] == key:
                return True
            current = current.next
        else:
            return False
        
    def remove(self, key):
        if self.head.data[0] == key:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        while current.next != None:
            if current.next.data[0] == key:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
        else:
            raise NotFoundException()
        
    def __setitem__(self, key, data):
        if self.contains(key):
            self.update(key, data)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        return self.find(key)
    
    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        current = self.head
        while current != None:
            ret_str += str(current.data[0]) + " : " + str(current.data[1]) + ", "
            current = current.next
        return ret_str
    

class HashMap:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.buckets = [Bucket() for i in range(self.capacity)]

    def rebuild(self):
        self.capacity *= 2
        new_buckets = [Bucket() for i in range(self.capacity)]
        for bucket in self.buckets:
            current = bucket.head
            while current != None:
                index = self.compression(current.data[0])
                bucket = new_buckets[index]
                bucket.insert(current.data[0], current.data[1])
                current = current.next
        self.buckets = new_buckets

    def compression(self, key):
        return hash(key) % self.capacity


    def insert(self, key, data):
        if self.contains(key):
            raise ItemExistsException()
        if self.size > 1.2 * self.capacity:
            self.rebuild()
        index = self.compression(key)
        self.buckets[index].insert(key, data)
        self.size += 1

    def update(self, key, data):
        if not self.contains(key):
            raise NotFoundException()
        self.buckets[hash(key) % self.capacity].update(key, data)

    def find(self, key):
        return self.buckets[hash(key) % self.capacity].find(key)
    
    def contains(self, key):
        return self.buckets[hash(key) % self.capacity].contains(key)
    
    def remove(self, key):
        self.buckets[hash(key) % self.capacity].remove(key)
        self.size -= 1

    def __setitem__(self, key, data):
        if self.contains(key):
            self.update(key, data)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        return self.find(key)
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        ret_str = ""
        for bucket in self.buckets:
            ret_str += str(bucket) + "\n"
        return ret_str
    

        

    

    