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
                self.size -= 1
                return node.right
            elif node.right == None:
                self.size -= 1
                return node.left
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
    
if __name__ == "__main__":
   pass