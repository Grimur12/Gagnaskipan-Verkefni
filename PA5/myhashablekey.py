class MyHashableKey:
    def __init__(self, int_value, string_value):
        self.i = int_value
        self.s = string_value

    def __eq__(self, other):
        return self.i == other.i and self.s == other.s
    
    def __hash__(self):
        return self.i % 10
    
