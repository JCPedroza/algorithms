# http://dbader.org/blog/functional-linked-lists-in-python
"""
Constructing linked lists

Our linked list data structure consists of two fundamental building blocks: Nil and cons. Nil represents the 
empty list and serves as a sentinel for more complex lists. The cons operation extends a list at the front by 
inserting a new value.

The lists we construct using this method consist internally of nested 2-tuples. For example, the list [1, 2, 3] 
is represented by the expression cons(1, cons(2, cons(3, Nil))) which evaluates to the nested tuples (1, (2, (3, Nil))).
"""

Nil = None

def cons(head, tail=Nil):
    return (head, tail)

"""
Abstracting away the tuple construction using the cons function gives us a lot of flexibility on how lists are 
represented internally as Python objects. For example, instead of using 2-tuples we could store our elements in 
a chain of anonymous functions using Pythons lambda keyword.
"""
def lst(*xs):
    """
    Define list instances using a more convenient syntax and without deeply nested cons calls.
    lst() == Nil
    lst(1, 2, 3) == (1, (2, (3, Nil))) 
    """
    if not xs:
        return Nil
    else:
        return cons(xs[0], lst(*xs[1:]))

def head(xs):
    """ Returns the frst element of a list. """
    return xs[0]

def tail(xs):
    """ Returns a list containing all elements except the first. """
    return xs[1]

def is_empty(xs):
    """ Returns True if the list contains zero elements """
    return xs is Nil

def length(xs):
    """
    Returns number of elements in a given list. To find the length of a list we need to scan all of its
    elements, thus leading to a time complexity of O(n).
    """
    if is_empty(xs):
        return 0
    else:
        return 1 + length(tail(xs))

def concat(xs, ys):
    """ Concatenates two lists. O(n) """
    if is_empty(xs):
        return ys
    else:
        return cons(head(xs), concat(tail(xs), ys))

def last(xs):
    """ Returns last element of a non-empty list. O(n) """
    if is_empty(tail(xs)):
        return head(xs)
    else:
        return last(tail(xs))

def init(xs):
    """ Returns all elements except the last one. O(n) """
    if is_empty(tail(tail(xs))):
        return cons(head(xs))
    else:
        return cons(head(xs), init(tail(xs)))

def reverse(xs):
    """ Returns the input list, reversed. O(n*2) """
    if is_empty(xs):
        return xs
    else:
        return concat(reverse(tail(xs)), cons(head(xs), Nil))

# !!! Can this be improved?
def sub_from(xs, from_index):
    """ Creates a sublist of the input list that includes the items from_index onwards  """
    if is_empty(xs):
        return xs
    elif from_index < 1:
        return cons(head(xs), sub_from(tail(xs), from_index))
    else:
        return sub_from(tail(xs), from_index - 1)

# !!! Can this be improved?
def sub_to(xs, to_index):
    """ Creates a sublist of the input list that includes the items up to to_index """
    if to_index < 0:
        return Nil
    else:
        return cons(head(xs), sub_to(tail(xs), to_index - 1))

def sub_from_to(xs, from_index, to_index):
   pass

def remove_index(xs, index):
    """ Returns a copy of the input list which doesn't contain the node in the specified index """
    return concat(sub_to(xs, index - 1), sub_from(xs, index + 1))

# Examples:

a = lst(1, 2, 3, 4)
b = lst(5, 6, 7, 8)
ab = concat(a, b)
print a
print head(a)
print tail(a)
print is_empty(a)
print length(a)
print last(ab)
print init(ab)
print reverse(ab)
print sub_from(a, 1)
print remove_index(a, 1)
print sub_to(ab, 4)
print remove_index(ab, 8)


