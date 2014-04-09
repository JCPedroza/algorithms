"""
Immutable linkeds lists, oop approach.

A fundamental data structure in many functional languages is the immutable
linked list. It is constructed from two building blocks:

Nil: the empty list.
Cons: a cell containing an element and the remainder of the list.

A list is either an empty list new Nil or a list new Cons(x, xs)
consisting of a head element x and a tail list xs.
"""

class Cons:
    """
    Cons cell is a cell that is not empty; it contains an item.
    Since head and tail are declared and initialized in the  class declaration
    using val, they don't need to be declared in the class' body. In Scala,
    val can override def, the difference between them concerns only the
    initialization: def by name and val by value.
    """
    def __init__(self, head, tail):
        self.head = head  # item in the cell
        self.tail = tail  # rest of the list

    def __str__(self):
        return str(self.head) + ", " + str(self.tail)

    def is_empty(self):
        return False     # a Cons cell is never empty

class Nil:
    """ Class for an empty cell """
    def __str__(self):
        return "Nil"

    def is_empty(self):
        return True     # a Nil cell is always empty
    
    def head(self):
        raise Exception("Nil.head")  # Nil cells do not have items

    def tail(self):
        raise Exception("Nil.tail")  # Nil cells do not have tail
    


def nth(n, a_list):
    """ Returns the nth element of a list """
    if a.is_empty:
        raise Exception("Index out of bounds")
    elif n == 0:
        return a_list.head
    else:
        nth(n - 1, a_list.tail)

# Examples of constructing linked lists
a = Cons(1, Nil())
b = Cons(2, a)
c = Cons(3, b)

print c  # 3, 2, 1, Nil



