"""
Python definition of navigable Tree class
"""

import tree


class NavTree(tree.Tree):
    """
    Recursive definition for navigable trees plus extra tree methods
    """

    def __init__(self, value, children, parent=None):
        """
        Create a tree whose root has specific value (a string)
        children is a list of references to the roots of the children.
        parent (if specified) is a reference to the tree's parent node
        """

        tree.Tree.__init__(self, value, children)
        self._parent = parent
        for child in self._children:
            child._parent = self

    def set_parent(self, parent):
        """
        Update parent field
        """
        self._parent = parent

    def get_root(self):
        """
        Return the root of the tree
        """
        if self._parent is None:
            return self
        else:
            return self._parent.get_root()

    def depth(self):
        """
        Return the depth of the self with respect to the root of the tree
        """
        if self._parent is None:
            return 0
        else:
            return self._parent.depth() + 1
