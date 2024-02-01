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
        
        # Kennarinn segir í videoinu að maður ætti kanski að hafa capacity og size kanski byrja a capacity = 4
        # Þá þegar size == capacity þá resize() og resize stækkar capacity og þa getum við haldið áfram

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
        # Nota insert fallið til að prependa 
        # eithvað eins og self.insert(value, 0)
        self.insert(value,0)

        ## Virkar        

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        # þarf að innihalda if index < 0 eða > self.size þá raise IndexOutOfBounds()
        # Ef það á að inserta í arrayið þá þýðir það að það er verið að stækka það, erum með function resize sem á að gera það
        # ef við stækkum alltaf listann um +1 í resize þá gætum við alltaf bara kallað á það í þessu falli
        # Pæling hvort maður ætti þá að hækka size um +1 í þessu falli eða í resize
        # í lokinn á insert þarf að bæta 1 við size , self.size += 1
        
        """
        def resize(array):
            array.append(0)
            return array

        def insert(array, value, index, size):
            array = resize(array)
            for i in range(size, index, -1):
                array[i] = array[i - 1]

            array[index] = value
            return array

        arr = [1,2,3,4,5,6,7,8,9,10]
        arr = insert(arr,23,4,len(arr))
        print(arr)
        """
        # Þetta myndi virka, köllum á resize() fyrst
        # Ættum að fá nýjann array með auka 0 aftaná megum ekki nota append í þessu samt
        # Ef við erum alltaf með síðasta stakið 0 aftast þá iterateum við í gegnum arrayið
        # byrjum á aftasta sem væri þá size, niðri indexinn sem við viljum breyta, og förum alltaf 1 skref til baka með -1
        # Overrideum síðan stakið sem er á i s.s aftast með stakinu sem er á bavkið þannig hverfur 0'ið aftast og á endanum verður auka stak í indexinum sem við viljum
        # Þá bara overridea það sér með self.arr[index] = value
        # Virkar bara ef resize hefur 0 aftaná
        # síðan self.size += 1

        if self.size == self.capacity:
            self.resize()
            
        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i-1]
        
        self.arr[index] = value

        self.size += 1

        ## Virkar

    #Time complexity: O(1) - constant time
    def append(self, value):
        # Sama og með prepend
        # self.insert(value,self.size) # setja stakið aftast á arrayið

        self.insert(value,self.size)

        ## Virkar

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # Getum sliceað arrayið og sett í staðin
        # self.arr[index] = value
        # if index < 0 eða > self.size þá raise IndexOutOfBounds()
        if index < 0 or index > self.size:
            raise IndexOutOfBounds()

        self.arr[index] = value

        ## Virkar

    #Time complexity: O(1) - constant time
    def get_first(self):
        # Slicea arrayið
        # return self.arr[0] 
        # if self.size (stærðin á arrayinu) == 0 þá raise Empty()
        if self.size == 0:
            raise Empty()
        return self.arr[0]
    
        ## Virkar

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # slicea arrayið
        # getum gert sama og í set_at s.s if index < 0 eða > self.size þá raise IndexOutOfBounds()
        # return self.arr[index]

        if index < 0 or index > self.size:
            raise IndexOutOfBounds()
        
        return self.arr[index]
    
        ## Virkar

    #Time complexity: O(1) - constant time
    def get_last(self):
        # Slicea arrayið
        # getum gert sama og í get_first s.s if self.size (stærðin á arrayinu) == 0 þá raise Empty()
        # return self.arr[-1] eða self.arr[self.size -1] ef [-1] er ekki leyfilegt held að það sé það samt
        return self.arr[-1]
        
        ## Virkar

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

        # stækka arrayið sé ekki hvort það standi hversu mikið það eigi að vera
        # gera nýtt array
        # new_arr = [0] * (1+self.size eða hversu mikið hann á að stækka um)
        # for loopa yfir gamla arrayið ? kanski má það ekki.. new_array[i] = self.array[i]
        # Síðan overridea self.array, sef.array = new_array

        ## Virkar

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # Sama og get_at
        # Slicea arrayið
        # Gætum búið til for lykkju sem fer yfir allt arrayið frá indexinum sem við viljum taka stakið frá og uppí endann eða næst síðasta stakið afþví við erum að taka 1 í burtu
        # síðan overridea stakið sem er á indexinum fyrir næsta stak
        # Þannig for i in range(index, self.size - 1) og siðan self.arr[i] = self.arr[i+1] síðan þarf að minka size um 1, kanski má þetta ekki, veit ekki hvort það megi hafa for loopur
        # Önnur leið væri að bara slicea listann uppað indexinu og frá indexinu og bæta saman
        # self.arr = self.arr[:index] + self.arr[index+1:] og síðan taka 1 fra size, self.size -= 1, held að þetta megi ekki
        if index < 0 or index > self.size:
            raise IndexOutOfBounds()

        for i in range(index, self.size - 1):
            self.arr[i] = self.arr[i+1]
        
        self.size -= 1

        ## Virkar


    #Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0
        
        ## Virkar

    def Linear_Search(self, value):
        if not self.arr:
            return False
        
        if self.arr[0] == value:
            return True
    
        return Linear_Search(self.arr[1:], value)

    def Binary_search(self, value):
    # Base case: if the string is empty, the element is not found
        if not value:
            return False
        else:
            # Calculate the mid index and compare the middle element with the target
            mid = self.size // 2
            if self.arr[mid] == value:
                return True
            elif self.arr[mid] > value:
                # Recursive case: search in the left half of the string
                return Binary_search(self.arr[:mid], value)
            else:
                # Recursive case: search in the right half of the string
                return Binary_search(self.arr[mid+1:], value)

    def check_ordered(self):
        for i in range(self.size-1):
            if self.arr[i] > self.arr[i+1]:
                return False
        return True
            

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # Er manneskjan alltaf að setja inn hærri tölu
        # Eða þarf að leita í arrayinu eftir réttum stað fyrir töluna og siðan insert() ?
        # Gera fall sem tjékkar hvort i+1 < i
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # Ef Arrayið er sorted þá recursive binary search
        # Ef arrayið er ekki sorted þá linear
        # Má bæta við function i klasann sem er lin search og bin search og ordered checker ?
    
        pass

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


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
    arr_lis.clear()
    print(arr_lis, "Cleared")