class NotFoundException(Exception):
    pass

class ItemExistsException(Exception):
    pass

class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BSTMap:
    def __init__(self):
        self.root = None
        self.size = 0

    def _insert_rec(self, node, key, value):
        if node == None:
            self.size += 1
            return BSTNode(key, value)
        elif key < node.key:
            node.left = self._insert_rec(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_rec(node.right, key, value)
        else:
            raise ItemExistsException
        return node
    
    def insert(self, key, value):
        self.root = self._insert_rec(self.root, key, value)
    
    def _update_rec(self, node, key, value):
        if node == None:
            raise NotFoundException
        elif key < node.key:
            node.left = self._update_rec(node.left, key, value)
        elif key > node.key:
            node.right = self._update_rec(node.right, key, value)
        else:
            node.value = value
        return node
    
    def update(self, key, value):
        self.root = self._update_rec(self.root, key, value)

    def _find_rec(self, node, key):
        if node == None:
            raise NotFoundException
        elif key < node.key:
            return self._find_rec(node.left, key)
        elif key > node.key:
            return self._find_rec(node.right, key)
        else:
            return node.value
        
    def find(self, key):
        return self._find_rec(self.root, key)
    
    def contains(self, key):
        try:
            self.find(key)
            return True
        except NotFoundException:
            return False
        
    def _remove_rec(self, node, key):
        if node == None:
            raise NotFoundException
        if key < node.key:
            node.left = self._remove_rec(node.left, key)
        elif key > node.key:
            node.right = self._remove_rec(node.right, key)
        else:
            if node.left == None:
                temp = node.right
                node = None
                self.size -= 1
                return temp
            elif node.right == None:
                temp = node.left
                node = None
                self.size -= 1
                return temp
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._remove_rec(node.right, temp.key)
        return node
    
    def remove(self, key):
        self.root = self._remove_rec(self.root, key)

    def _min_value_node(self, node):
        current = node
        while current.left != None:
            current = current.left
        return current
    
    def __setitem__(self, key, value):
        try:
            self.update(key, value)
        except NotFoundException:
            self.insert(key, value)

    def __getitem__(self, key):
        return self.find(key)
    
    def _inorder_traversal(self, node, result):
        if node != None:
            self._inorder_traversal(node.left, result)
            result.append((node.key, node.value))
            self._inorder_traversal(node.right, result)

    def __str__(self):
        result = []
        self._inorder_traversal(self.root, result)
        formatted_result = ' '.join(f'{{{key}:{value}}}' for key, value in result)
        return formatted_result


    def __len__(self):
        return self.size
    
## f __name__ == "__main__":
##    print("\nTESTING BSTMAP Remove")
##    m = BSTMap()
##    try:
##        m.insert(6, "sexa")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(4, "fjarki")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(2, "tvistur")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(5, "fimma")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(8, "átta")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(7, "sjöa")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(9, "nía")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(3, "þristur")
##    except ItemExistsException:
##        print("Item already exists")
##    print("size of map: " + str(len(m)))
##    print(m)
##    print("--Remove--")
##    try:
##        m.remove(4)
##        print("Item removed 4")
##    except NotFoundException:
##        print("Item not found")
##    print("size of map: " + str(len(m)))
##    print(m)
##    try:
##        m.remove(3)
##        print("Item removed 3")
##    except NotFoundException:
##        print("Item not found")
##    print("size of map: " + str(len(m)))
##    print(m)
##    try:
##        m.remove(5)
##        print("Item removed 5")
##    except NotFoundException:
##        print("Item not found")
##    print("size of map: " + str(len(m)))
##    print(m)
##    try:
##        m.remove(9)
##        print("Item removed 9")
##    except NotFoundException:
##        print("Item not found")
##    print("size of map: " + str(len(m)))
##    print(m)
##    try:
##        m.remove(8)
##        print("Item removed 8")
##    except NotFoundException:
##        print("Item not found")
##    print("size of map: " + str(len(m)))
##    print(m)
##    try:
##        m.remove(7)
##        print("Item removed 7")
##    except NotFoundException:
##        print("Item not found")
##    print("size of map: " + str(len(m)))
##    print(m)
##    try:
##        m.remove(6)
##        print("Item removed 6")
##    except NotFoundException:
##        print("Item not found")
##    print("size of map: " + str(len(m)))
##    print(m)
##    try:
##        m.remove(2)
##        print("Item removed 2")
##    except NotFoundException:
##        print("Item not found")
##    print("size of map: " + str(len(m)))
##    print(m)
##    try:
##        m.remove(5)
##        print("Item removed 5")
##    except NotFoundException:
##        print("Item not found")
##    print("size of map: " + str(len(m)))
##    print(m)
## 
##    print("\nTESTING BSTMAP Contains")
##    m = BSTMap()
##    try:
##        m.insert(6, "sexa")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(4, "fjarki")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(2, "tvistur")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(5, "fimma")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(8, "átta")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(7, "sjöa")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(9, "nía")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(3, "þristur")
##    except ItemExistsException:
##        print("Item already exists")
##    print("size of map: " + str(len(m)))
##    print(m)
##    print("Contains 6:", m.contains(6))
##    print("Contains 4:", m.contains(4))
##    print("Contains 2:", m.contains(2))
##    print("Contains 5:", m.contains(5))
##    print("Contains 8:", m.contains(8))
##    print("Contains 7:", m.contains(7))
##    print("Contains 9:", m.contains(9))
##    print("Contains 3:", m.contains(3))
##    print("Contains 1:", m.contains(1))
##    print("Contains 0:", m.contains(0))
##    print("Contains 10:", m.contains(10))
##    print("Contains 11:", m.contains(11))
##    print("Contains 12:", m.contains(12))
##    print("Contains 13:", m.contains(13))
##    print("Contains 14:", m.contains(14))
##    print("Contains 15:", m.contains(15))
##    print("Contains 16:", m.contains(16))
##    print("Contains 17:", m.contains(17))
##    
## 
##    print("\nTESTING BSTMAP Update")
##    m = BSTMap()
##    try:
##        m.insert(6, "sexa")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(4, "fjarki")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(2, "tvistur")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(5, "fimma")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(8, "átta")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(7, "sjöa")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(9, "nía")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(3, "þristur")
##    except ItemExistsException:
##        print("Item already exists")
##    print("size of map: " + str(len(m)))
##    print(m)
##    m.update(6, "sexi")
##    print(m)
##    m.update(4, "fjarkur")
##    print(m)
##    m.update(2, "tvist")
##    print(m)
##    m.update(5, "fimmi")
##    print(m)
##    m.update(8, "átur")
##    print(m)
##    m.update(7, "sjö")
##    print(m)
##    m.update(9, "níu")
##    print(m)
##    m.update(3, "þrí")
##    print(m)
## 
## 
##    print("\nTESTING BSTMAP Insert")
##    m = BSTMap()
##    try:
##        m.insert(6, "sexa")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(4, "fjarki")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(2, "tvistur")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(5, "fimma")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(8, "átta")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(7, "sjöa")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(9, "nía")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(3, "þristur")
##    except ItemExistsException:
##        print("Item already exists")
##    print("size of map: " + str(len(m)))
##    print(m)
##    try:
##        m.insert(6, "sexi")
##    except ItemExistsException:
##        print("Item already exists")
##    print("size of map: " + str(len(m)))
##    print(m)
##    try:
##        m.insert(4, "fjarkur")
##    except ItemExistsException:
##        print("Item already exists")
##    print("size of map: " + str(len(m)))
##    print(m)
##    try:
##        m.insert(2, "tvist")
##    except ItemExistsException:
##        print("Item already exists")
##    print("size of map: " + str(len(m)))
##    print(m)
##    try:
##        m.insert(5, "fimmi")
##    except ItemExistsException:
##        print("Item already exists")
##    print("size of map: " + str(len(m)))
##    print(m)
##    try:
##        m.insert(10, "tían")
##    except ItemExistsException:
##        print("Item alread exists")
##    print("size of map: " + str(len(m)))
##    print(m)
##    try:
##        m.insert(10, "tían")
##    except ItemExistsException:
##        print("Item alread exists")
##    print("size of map: " + str(len(m)))
##    print(m)
## 
## 
##    print("\nTESTING BSTMAP Find")
##    m = BSTMap()
##    try:
##        m.insert(6, "sexa")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(4, "fjarki")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(2, "tvistur")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(5, "fimma")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(8, "átta")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(7, "sjöa")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(9, "nía")
##    except ItemExistsException:
##        print("Item already exists")
##    try:
##        m.insert(3, "þristur")
##    except ItemExistsException:
##        print("Item already exists")
##    print("size of map: " + str(len(m)))
##    print(m)
##    print("Find 6:", m.find(6))
##    print("Find 4:", m.find(4))
##    print("Find 2:", m.find(2))
##    print("Find 5:", m.find(5))
##    print("Find 8:", m.find(8))
##    print("Find 7:", m.find(7))
##    print("Find 9:", m.find(9))
##    print("Find 3:", m.find(3))



