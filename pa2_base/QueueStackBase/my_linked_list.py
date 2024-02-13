class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    # O(1)
    def push_front(self, data):
        new_node = Node(data)
        if self.head == None: # Listinn er tómur
            self.head = new_node # fyrsta stakið er nýtt node með datainu
            self.tail = new_node # síðasta stakið er nýtt node með datainu ef listinn er tómur þá er þetta natturulega bara sama stakið og það er ekkert .next
        else:
            new_node.next = self.head # Ef það eru núþegar stök þá er næsta stakið þá þar sem var áður fyrsta 
            self.head = new_node # og síðan er nýja nodeið með datainu sett inn fyrst
        self.size += 1 # Size + 1
    # O(1)
    def pop_front(self):
        if self.head == None: # Ef listinn er tómur þa bara None
            return None
        else:
            removed_node = self.head.data # Við erum að taka stakið sem var ýtt inn annaðhvort síðast með push_front() eða fyrst með push_back
            self.head = self.head.next # nýja fyrsta stakið í listanum er þá þar sem var áður næsta stakið
            self.size -= 1 # minnka size um 1
            return removed_node
    # O(1)
    def push_back(self, data):
        new_node = Node(data)
        if self.head == None: # Listinn er tómur
            self.head = new_node # Fyrsta stakið er bara nýtt node með datainu
        else: # Ef listinn er ekki tómur
            self.tail.next = new_node # Ef listinn er ekki tómur þá er self.tail.next = new_node og next í því er default None þannig það verður None
        self.tail = new_node # Lætur self.tail eða síðasta stakið fá dataið inní new_node sem er stakið sem við viljum appenda
        
        self.size += 1
    # O(n)
    def pop_back(self):
        # Kanski litið það betur út að hafa current_node.next != self.tail og hafa þa removed_node alltaf bara = self.tail.data
        # Þetta er ekki tested gæti verið sma vitlaust
        # if self.head == None:
        #     return None
        
        # removed_node = self.tail.data

        # if self.head == self.tail:
        #     self.tail = None
        #     self.head = None
        #     self.size -= 1
        #     return removed_node

        # current_node = self.head

        # while current_node.next != self.tail: # Ef stakið bendir á self.tail þá erum við komnir á næst siðasta stakið og current_node er þá næstsíðasta
        #     current_node = current_node.next
        # self.tail.next = None
        # self.tail = current_node
        # self.size -1
        # return removed_node

        if self.head == None:
            return None
        
        current_node = self.head
        # Þarf að hafa condition fyrir þegar það er bara 1 node afþví þá virkar ekki stóra while lykkjan hún þaf amk 2 stök
        if current_node.next == None:
            removed_node = current_node.data
            self.tail = None
            self.head = None
            self.size -= 1
            return removed_node

        while current_node.next.next != None: # Loopar þangað til stak bendir á annað stak og það bendir á none, það fer samt í það loop
            current_node = current_node.next # Ef stakið bendir á annað stak sem bendir ekki á None þá heldur afram
        #Current node verður þá næst síðasta og current.node.next = síðasta current.node.next.next er None
        removed_node = current_node.next.data
        self.tail = current_node  # current_node.next ætti að vera næst síðasta stakið þannig gera self.tail = current_node er þá síðasta stakið
        # self.tail.next er samt enþá næsta Node þannig það þarf None , kanski er betri leið til að gera þetta ?
        self.tail.next = None
        self.size -= 1
        return removed_node

    # O(1)
    def get_size(self):
        return self.size
    # O(n)
    def __str__(self):
        # Gæti þurft að laga print fallið veit ekki hvernig það á að lýta út. þetta er fyrir testing
        ret_str = ""
        current_node = self.head
        while current_node != None:
            ret_str += str(current_node.data) + " "
            current_node = current_node.next
        return ret_str
