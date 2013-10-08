/**
* Purely functional integer set, implementing something similar to binary search tree, but with duplicate
* nodes; left side must be empty or a value smaller than the parent, and right side must be empy or a value
* greater than the parent.
*
* This implementation does no mutation. When we call incl we create a new tree that contains the previous
* element of the tree.
*
* This is called a persitent data sctructure, because even when we do changes, the old version of the data
* structure is still mantained. Persitent data structures are one of the cornerstones of scalable
* functional programming.
*
* Example:
*
* When we say we include an element on the left sub-tree what we really mean is that
* we create a new tree that contains the previous element of the tree and a larger left sub-tree where x
* is included in the previous left sub-tree, and the current sub-tree on the right.
*
* We have  this binary tree (no branch means empty subtree):
*        7
*       /\
*      5  12
*          /\
*         9  13
* Tree after incl(3):
*          7
*       /  7 \
*      5  / \ |
*     /  5  12
*    3      /\
*          9  13
* A new node 3 is created, with two empty subtrees. That subtree will be the left subtree of a new node 5
* that has an empty right side. New node 7 is created, which left side links to 5, and right side links to
* the same place as the old 7: 12.
*/
object IntFunSetsBinaryT {
  val t1 = new NonEmpty(3, Empty, Empty)          //> t1  : NonEmpty = {.3.}
  val t2 = t1 incl 4                              //> t2  : IntSet = {.3{.4.}}
}

abstract class IntSet{
  def incl(x: Int): IntSet         // include element x in the IntSet
  def contains(x: Int): Boolean    // is x an element of the set?
  def union(other: IntSet): IntSet // union of this and other set
}

/**
* Represents an empty node.
* There is really only a single empty IntSet, so it seems overkill to have the user
* create many instances of it. That's why we implement Empy as a singleton object.
*/
object Empty extends IntSet{
  def contains(x: Int): Boolean = false
  def incl(x:Int): IntSet = new NonEmpty(x, Empty, Empty)
  override def toString = "."
  def union(other:IntSet): IntSet = other
}

class NonEmpty(elem: Int, left: IntSet, right: IntSet) extends IntSet{

  def contains(x: Int): Boolean =
    if      (x < elem) left contains x
    else if (x > elem) right contains x
    else true
  
  // Calls nodes until it reaches an empty node, where x is included.  
  def incl(x: Int): IntSet =
    if      (x < elem) new NonEmpty(elem, left incl x, right)
    else if (x > elem) new NonEmpty(elem, left, right incl x)
    else this
    
  override def toString = "{" + left + elem + right + "}"
  
  def union(other:IntSet): IntSet =
    ((left union right) union other) incl elem
  
}