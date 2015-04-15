"""
Python definition of basic Tree class

IMPORTANT:  Some class methods assume that instances of the Tree class
always have a single parent (or no parent for the root).
"""


class Tree:
    """
    Recursive definition for trees plus various tree methods
    """

    def __init__(self, value, children):
        """
        Create a tree whose root has specific value (a string)
        Children is a list of references to the roots of the subtrees.
        """

        self._value = value
        self._children = children

    def __str__(self):
        """
        Generate a string representation of the tree
        Use an pre-order traversal of the tree
        """

        ans = "["
        ans += str(self._value)

        for child in self._children:
            ans += ", "
            ans += str(child)
        return ans + "]"

    def get_value(self):
        """
        Getter for node's value
        """
        return self._value

    def children(self):
        """
        Generator to return children
        """
        for child in self._children:
            yield child

    def num_nodes(self):
        """
        Compute number of nodes in the tree
        """
        ans = 1
        for child in self._children:
            ans += child.num_nodes()
        return ans

    def num_leaves(self):
        """
        Count number of leaves in tree
        """
        if len(self._children) == 0:
            return 1

        ans = 0
        for child in self._children:
            ans += child.num_leaves()
        return ans

    def height(self):
        """
        Compute height of a tree rooted by self
        """
        height = 0
        for child in self._children:
            height = max(height, child.height() + 1)
        return height
