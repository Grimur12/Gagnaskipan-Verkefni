class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Node():
    
    def __init__(self, key, data):
        # Læt key vera það sem er í trénú og dataið vera tengt við, inserta m.v key svo að ég geti prentað út inorder og þa er það ordered
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BSTMap():

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, data):
        # Ef tréð er tómt þarf ekkert að gá þannig bara setja new_node sem rótina
        if self.root is None:
            self.root = Node(key, data)
            self.size += 1
        # Ef tréð er ekki tómt þarf að gá hvort key sé til staðar og annaðhvort setja hægri eða vinstri við root
        else:
            self._insert_recur(self.root, key, data)

    def _insert_recur(self, node, key, data):
        # Ef node.key er til þá gera exception, viljum engin duplicates, hafa í recur því að gáum að öllum nóðum meðan við förum neðar í tréinu
        if node.key == key:
            raise ItemExistsException()
        # Ef key < node.key þá fer nýja nodeið til vinstri
        elif key < node.key:
            # Ef vinstra nodeið er tómt þá fer nýja nodeið beint þangað ef ekki þá fer einum neðar með recur
            if node.left is None:
                node.left = Node(key, data)
                self.size += 1
            else:
                self._insert_recur(node.left, key, data)
        # Ef key > node.key þá fer nýja nodeið til hægri
        else:
            # Ef hægra nodeið er tómt þá fer nýja nodeið beint þangað ef ekki þá fer einum neðar með recur
            if node.right is None:
                node.right = Node(key, data)
                self.size += 1
            else:
                self._insert_recur(node.right, key, data)

    def update(self, key, data):
        # Þarf að finna réttu nóðuna og breyta data í því
        # Erum með find function, nota það
        # Ef nóðan er til staðar þá breyta datainu í henni, ef ekki þá exception
        node = self._find_recur(self.root, key)
        if node is None:
            raise NotFoundException()
        else:
            node.data = data

    def find(self, key):
        node = self._find_recur(self.root, key)
        if node is None:
            raise NotFoundException()
        return node.data

    def _find_recur(self, node, key):
        # Fyrir Exception ef node er tóm þá return None
        if node is None:
            return None
        # Förum recursively niður tréð þangað til við hittum á key sem við viljum og skilum þá þeirri nóðu
        # Ef node.key == key skila node
        if node.key == key:
            return node
        # Ef key < node.key þá förum við til vinstri að leita
        elif key < node.key:
            return self._find_recur(node.left, key)
        # Ef ekki þá er key > node.key og förum til hægri að leita
        else:
            return self._find_recur(node.right, key)

    def contains(self, key):
        # getum líklega notað find hér líka
        # Getum notað find til að gá hvort við raiseum exception
        # Eða notað recur fallið beint afþví ef node finnst ekki þa faum við None
        node = self._find_recur(self.root, key)
        if node is None:
            return False
        else:
            return True

    def remove(self, key):
        if self._find_recur(self.root,key):
            self.root = self._remove_recur(self.root, key)
            self.size -=1
        else:
            raise NotFoundException()
        

    def _remove_recur(self, node, key):
        # Tilfelli 1: nóða sem á að removea er lauf, ekki með neitt left né right: þarf að láta nóðuna fyrir ofan benda á None
        # Tilfelli 2: nóða sem á að removea er með 1 nóðu til hægri eða vinstri, láta nóðuna fyrir ofan nóðuna sem á að removea benda á nóðuna fyrir neðan hana sem á að removea
        # Tilfelli 3: nóða sem á að removea er með nóðu til hægri og vinstri, finna nóðuna lengst til hægri í vinstra tréinu, swappa henni við það sem á að removea og síðan er það alveg eins og í tilviki annaðhvort 1 eða 2, afþví sú nóða gæti verið lauf eða verið með 1 barn á visntri
        # Finna nóðuna sem við viljum removea
        if key < node.key:
            node.left = self._remove_recur(node.left, key)
        elif key > node.key:
            node.right = self._remove_recur(node.right, key)
        else:
            if node.right is None: # Tilfelli 2
                return node.left
            elif node.left is None: # Tilfelli 2
                return node.right
            #Tilfelli 3
            rightmost = self.find_rightmost_node_recur(node.left)

            node.data = rightmost.data
            node.key = rightmost.key

            node.left = self._remove_recur(node.left, rightmost.key)
        return node


    def find_rightmost_node_recur(self, node):
        # nóðan sem þetta fall tekur inn ætti að vera node.left
        # Fallið finnur lengstu nóðuna til hægri í vinstra tréinu sem við getum svo notað til að skipta
        # ef nóða er með bæði hægri og vinstri þá finna þessa nóðu og skipta á data og key 
        if node is None:
            return
        
        if node.right is None:
            return node
        else:
            return self.find_rightmost_node_recur(node.right)

    def __setitem__(self, key, data):
        # m[1] = "einn", key = 1, data = "einn" ef 1 er nuþegar key þá breyta data í 1, getum notað update ?
        # Ef 1 er ekki key þá þurfum að að inserta því í tréð með datainu nota insert
        # Gá hvort key sé í tréinu
        node = self._find_recur(self.root, key)
        # Ef key er ekki í tréinu þá insert
        if node is None:
            self.insert(key, data)
        # Ef í tréinu þá bara update
        else:
            self.update(key, data)

    def __getitem__(self, key):
        # data = m[key] fá dataið úr keyinum ef það er í tréinu
        # notum find aftur til að sjá hvort key sé í tréinu
        node = self._find_recur(self.root, key)
        # Ef key er ekki í tréinu þá exception
        if node is None:
            raise NotFoundException()
        # Ef hún er til staðar þá fundum við hana með find þurfum bara að skila data
        else:
            return node.data

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