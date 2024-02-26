class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def get_size(head):
    if head == None:
        return 0

    return 1 + get_size(head.next)

def reverse_list(head):
    if head == None:   # Ef listinn er tómur 
        return None # Return None
    elif head.next == None: # Ef listinn er með 1 stak
        return head # Þá er hann Palindrome og þá return head listi == reversed(listi)
    next_head = reverse_list(head.next) # Þetta kallar á recursionið þangað til það hittir á stakið þar sem head.next == None þá fer það að reversa 
    head.next.next = head # Head hérna er næst síðasta stakið í listanum, head.next er síðasta stakið í listanum og head.next.next er þá None, við breytum því í head þannig þá er síðasta stakið núna að benda í næst síðasta stakið þannig er þetta buið að reverseast
    head.next = None # Látum síðasta stakið í listanum benda á None, annars er þetta endalaust recursion

    return next_head

def palindrome_helper(front, current):
    if current is None: # Ef current er None þá er listinn búinn að fara í gegnum allt og er þá Palindrome
        return True, front # 
    is_palindrome, front = palindrome_helper(front, current.next) # Þetta kallar á recursionið þangað til það hittir á síðasta stakið í listanum
    if not is_palindrome or front.data != current.data: # Ef listinn er ekki Palindrome eða ef stakið sem front benti á er ekki sama og stakið sem current benti á þá er listinn ekki Palindrome
        return False, front
    return True, front.next # Ef listinn er Palindrome og stakið sem front benti á er sama og stakið sem current benti á þá skilar þetta True og næsta staki í listanum

def palindrome(head):
    ## Ekki tilbuið
    is_palindrome, _ = palindrome_helper(head, head) # Þetta kallar á helper functionið sem skilar True ef listinn er Palindrome annars False
    return is_palindrome


if __name__ == "__main__":
    ##
    print("GET_SIZE TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = None
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", None)
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", Node("C", None))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)


    ##
    print("REVERSE TESTS")
    print("\n")
    head = Node("A", Node("B", Node("C", Node("D", Node("E", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("A", Node("A", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", None)
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = None
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", None))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)


    ##
    print("PALINDROME TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

