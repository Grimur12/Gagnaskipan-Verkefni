
class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class SLLNode:
    def __init__(self, key, data, next = None):
        self.key = key
        self.data = data
        self.next = next

class Bucket:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, key, data):
        if self.contains(key):
            raise ItemExistsException()
        else:
            new_node = SLLNode(key, data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def update(self, key, data):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.key == key:
                curr_node.data = data
                return
            curr_node = curr_node.next
        raise NotFoundException()
    
    def find(self, key):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.key == key:
                return curr_node.data
            curr_node = curr_node.next
        raise NotFoundException()

    def contains(self, key):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.key == key:
                return True
            curr_node = curr_node.next
        return False

    def remove(self, key):
        if self.head and self.head.key == key:
            self.head = self.head.next
            self.size -=1
            return
        
        curr_node = self.head

        while curr_node is not None:
            if curr_node.next.key == key:
                curr_node.next = curr_node.next.next
                self.size -= 1
                return
            curr_node = curr_node.next
            
        raise NotFoundException()
    
    def __getitem__(self, key):
        return self.find(key)

    def __setitem__(self, key, data):
        if self.contains(key):
            self.update(key, data)
        else:
            self.insert(key, data)

    def __len__(self):
        return self.size
    
    def __str__(self):
        curr_node = self.head
        ret_str = ""
        while curr_node is not None:
            ret_str += f"{{{curr_node.key}:{curr_node.data}}}" + " "
            curr_node = curr_node.next
        return ret_str

class HashMap:
    def __init__(self):
        self.capacity = 4
        self.buckets = [Bucket() for _ in range(self.capacity)]
        self.size = 0

    def insert(self, key, data):
        if self.contains(key):
            raise ItemExistsException()
        # Ef key er núþegar í safninu þá exception
        if self.size > 1.2 * self.capacity:
            self.rebuild()
        index = self.compress(key)
        self.buckets[index].insert(key, data)
        self.size += 1
    
    def compress(self, key):
        return hash(key) % self.capacity

    def rebuild(self):
        temp_buckets = self.buckets
        self.capacity *= 2
        self.size = 0
        self.buckets = [Bucket() for _ in range(self.capacity)]
        for buckets in temp_buckets:
            curr = buckets.head
            while curr:
                self.insert(curr.key, curr.data)
                curr = curr.next

    def update(self, key, data):
        index = self.compress(key)
        return self.buckets[index].update(key, data)

    def find(self, key):
        index = self.compress(key)
        return self.buckets[index].find(key)

    def contains(self, key):
        index = self.compress(key)
        return self.buckets[index].contains(key)

    def remove(self, key):
        index = self.compress(key)
        self.buckets[index].remove(key)
        self.size -= 1

    def __getitem__(self, key):
        return self.find(key)

    def __setitem__(self, key, data):
        try:
            self.update(key, data)
        except NotFoundException:
            self.insert(key, data)

    def __len__(self):
        return self.size
    
    def __str__(self):
        ret_str = ""
        for bucket in self.buckets:
            ret_str += str(bucket) + "\n"
        return ret_str

if __name__ == "__main__":
    b = Bucket()
    b.insert(1,"einn")
    b.insert(2,"tveir")
    b.insert(3,"þrir")
    b.insert(4,"fjorir")
    b.insert(5,"fimm")
    print(b)
    print(b.find(3))
    b.update(3, " ÞRIR")
    print(b.find(3))
    b[3] = "þrir"
    print(b.find(3))
    my_data = b[3]
    print(my_data)
    b.remove(1)
    print(b)
    b.remove(2)
    print(b)
    print(b.contains(4))
    b.remove(3)
    print(b)
    b.remove(5)
    print(b)
    b.remove(4)
    print(b)
    m = HashMap()
    print("TESTING HASHMAP")
    try:
        m.insert(5, "fimma")
    except ItemExistsException:
        print("Item already exists")
    try:
        m.insert(4, "fjarri")
    except ItemExistsException:
        print("Item already exists")
    try:
        m.insert(2, "tvistur")
    except ItemExistsException:
        print("Item already exists")
    try:
        m.insert(5, "fimmarimma")
    except ItemExistsException:
        print("Item already exists")
    m[1] = "ás"
    print(m)

    try:
        m.update(4, "fjarkalarki")
    except NotFoundException:
        print("Item not found")
    try:
        m.update(6, "sexxxxxa")
    except NotFoundException:
        print("Item not found")

    m[6] = "sexa"
    print(m)
    print("size of map: " + str(len(m)))
    print(m.contains(12))
    m[12] = "drottning"
    print(m.contains(12))

    print("size of map: " + str(len(m)))
    try:
        print(m.find(4))
    except NotFoundException:
        print("Item not found")
    try:
        print(m[2])
    except NotFoundException:
        print("Item not found")
    try:
        print(m[1])
    except NotFoundException:
        print("Item not found")
    try:
        print(m[5])
    except NotFoundException:
        print("Item not found")
    try:
        print(m.find(6))
    except NotFoundException:
        print("Item not found")
    try:
        print(m[7])
    except NotFoundException:
        print("Item not found")

    print("size of map: " + str(len(m)))
    try:
        m.remove(5)
        print("Item removed")
    except NotFoundException:
        print("Item not found")
    try:
        print(m.find(5))
    except NotFoundException:
        print("Item not found")
        
    print("size of map: " + str(len(m)))
