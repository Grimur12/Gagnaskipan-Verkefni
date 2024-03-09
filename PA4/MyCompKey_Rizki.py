class MyComparableKey:
    def __init__(self, int_value, string_value):
        self.int_value = int_value 
        self.string_value = string_value
    
    def __lt__(self, other):
        if self.int_value < other.int_value:  # við erum fyrst að bera saman int_value
            return True
        elif self.int_value > other.int_value:
            return False
        else:
            return self.string_value < other.string_value
        
