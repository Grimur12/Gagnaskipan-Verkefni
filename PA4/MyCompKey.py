
class MyComparableKey():
    
    def __init__(self, int_value, str_value) -> None:
        self.int_value = int_value
        self.str_value = str_value

    def __lt__(self, other):
        # Þetta er rétt útfært en kóðinn er ekki svakalega flottur, kanski hægt að gera á flottari hátt seinna
        if self.int_value < other.int_value:
            return True
        elif self.int_value == other.int_value:
            if self.str_value < other.str_value:
                return True
            else:
                return False
        else:
            return False

if __name__ == "__main__":
    pass
