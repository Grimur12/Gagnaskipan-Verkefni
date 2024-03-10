class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Node():
    
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BSTMap():

    def __init__(self):
        self.root = None
        self.size = 0

    def _insert_rec(self, node, key, data):
        if node == None:
            self.size += 1
            return Node(key, data)
        elif key < node.key:
            node.left = self._insert_rec(node.left, key, data)
        elif key > node.key:
            node.right = self._insert_rec(node.right, key, data)
        else:
            raise ItemExistsException
        return node
    
    def insert(self, key, data):
        self.root = self._insert_rec(self.root, key, data)

    def _update_recur(self, node, key, data):
        if node == None:
            raise NotFoundException
        elif key < node.key:
            node.left = self._update_recur(node.left, key, data)
        elif key > node.key:
            node.right = self._update_recur(node.right, key, data)
        else:
            node.data = data
        return node
    
    def update(self, key, value):
        self.root = self._update_recur(self.root, key, value)

    def find(self, key):
        return self._find_recur(self.root, key)

    def _find_recur(self, node, key):
        if node is None:
            raise NotFoundException
        elif key < node.key:
            return self._find_recur(node.left, key)
        elif key > node.key:
            return self._find_recur(node.right, key)
        else:
            return node.data

    def contains(self, key):
        try:
            self.find(key)
            return True
        except NotFoundException:
            return False

    def remove(self, key):
        self.root = self._remove_recur(self.root, key)

    def _remove_recur(self, node, key):
        if node is None:
            raise NotFoundException
        
        if key < node.key:
            node.left = self._remove_recur(node.left, key)
        elif key > node.key:
            node.right = self._remove_recur(node.right, key)
        else:
            if node.right is None:
                self.size -=1 
                return node.left
            elif node.left is None:
                self.size -=1 
                return node.right
            rightmost = self.find_rightmost_node_recur(node.left)

            node.data = rightmost.data
            node.key = rightmost.key

            node.left = self._remove_recur(node.left, rightmost.key)
        return node

    def find_rightmost_node_recur(self, node):
        if node is None:
            return
        
        if node.right is None:
            return node
        else:
            return self.find_rightmost_node_recur(node.right)

    def __setitem__(self, key, data):
        try:
            self.update(key, data)
        except NotFoundException:
            self.insert(key, data)

    def __getitem__(self, key):
        return self.find(key)

    def __len__(self):
        return self.size
    
    def _print_inorder_recur(self, node, ret_str = ""):
        if node is None:
            return ret_str
        ret_str = self._print_inorder_recur(node.left, ret_str)
        ret_str += f"{{{node.key}:{node.data}}}" + " "
        ret_str = self._print_inorder_recur(node.right, ret_str)
        return ret_str

    def __str__(self):
        return self._print_inorder_recur(self.root)

if __name__ == "__main__":
    print("\nTESTING BSTMAP Remove")
    m = BSTMap()
    try:
        m.insert(6, "sexa")
    except ItemExistsException:
        print("Item already exists")
    try:
        m.insert(4, "fjarki")
    except ItemExistsException:
        print("Item already exists")
    try:
        m.insert(2, "tvistur")
    except ItemExistsException:
        print("Item already exists")
    try:
        m.insert(5, "fimma")
    except ItemExistsException:
        print("Item already exists")
    try:
        m.insert(8, "átta")
    except ItemExistsException:
        print("Item already exists")
    try:
        m.insert(7, "sjöa")
    except ItemExistsException:
        print("Item already exists")
    try:
        m.insert(9, "nía")
    except ItemExistsException:
        print("Item already exists")
    try:
        m.insert(3, "þristur")
    except ItemExistsException:
        print("Item already exists")
    print("size of map: " + str(len(m)))
    print(m)
    print("--Remove--")
    try:
        m.remove(4)
        print("Item removed 4")
    except NotFoundException:
        print("Item not found")
    print("size of map: " + str(len(m)))
    print(m)
    try:
        m.insert(4,"fjarki")
        print("Item inserted 4")
    except NotFoundException:
        print("Item not found")
    print("size of map: " + str(len(m)))
    print(m)
    try:
        m[4] = "fjarrrrki"
        print("Item updated 4")
    except NotFoundException:
        print("Item not found")
    print("size of map: " + str(len(m)))
    print(m)
    try:
        m.remove(3)
        print("Item removed 3")
    except NotFoundException:
        print("Item not found")
    print("size of map: " + str(len(m)))
    print(m)
    try:
        m.remove(5)
        print("Item removed 5")
    except NotFoundException:
        print("Item not found")
    print("size of map: " + str(len(m)))
    print(m)
    try:
        m.remove(9)
        print("Item removed 9")
    except NotFoundException:
        print("Item not found")
    print("size of map: " + str(len(m)))
    print(m)
    try:
        m.remove(8)
        print("Item removed 8")
    except NotFoundException:
        print("Item not found")
    print("size of map: " + str(len(m)))
    print(m)
    try:
        m.remove(7)
        print("Item removed 7")
    except NotFoundException:
        print("Item not found")
    print("size of map: " + str(len(m)))
    print(m)
    try:
        m.remove(6)
        print("Item removed 6")
    except NotFoundException:
        print("Item not found")
    print("size of map: " + str(len(m)))
    print(m)
    try:
        m.remove(2)
        print("Item removed 2")
    except NotFoundException:
        print("Item not found")
    print("size of map: " + str(len(m)))
    print(m)
    try:
        m.remove(5)
        print("Item removed 5")
    except NotFoundException:
        print("Item not found")
    print("size of map: " + str(len(m)))
    print(m)
    try:
        m.remove(4)
        print("Item removed 5")
    except NotFoundException:
        print("Item not found")
    print("size of map: " + str(len(m)))
    print(m)
    try:
        m.remove(5)
        print("Item removed 5")
    except NotFoundException:
        print("Item not found")
    print("size of map: " + str(len(m)))
    print(m)
    m[4] = "F"
    print(m)
    try:
        m.find(3)
    except NotFoundException:
        print("Item not found")
    print(m[4])
    try:
        m[6]
    except NotFoundException:
        print("Item not found")