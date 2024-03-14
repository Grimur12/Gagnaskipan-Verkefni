class MyHashableKey:
    def __init__(self, int_value, string_value):
        self.i = int_value
        self.s = string_value

    def __eq__(self, other):
        return self.i == other.i and self.s == other.s
    
    def __hash__(self):
        return self.i + sum([ord(c) for c in self.s]) 
    # Þetta er hashið sem við notum til að hasha hlutina okkar. 
    # Við notum sum til að summa upp öll ascii gildi stafanna í strengnum og 
    # svo plúsum við við heiltöluna sem við fengum. Þetta er svo hashið sem 
    # við notum til að hasha hlutina okkar.
    
    
