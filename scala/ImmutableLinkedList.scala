/**
* A fundamental data structure in many functional languages is the immutable
* linked list. It is constructed from two building blocks:
* Nil: the empty list. 
* Cons: a cell containing an element and the remainder of the list.
* A list is either an empty list new Nil or a list new Cons(x, xs) 
* consisting of a head element x and a tail list xs. 
*/
object ImmutableLinkedList{

  /** returns the nth element of a list */ 
  def nth[T](n: Int, a: List[T]): T = {
    if      (a.isEmpty) throw new IndexOutOfBoundsException
    else if (n == 0)    a.head
    else                nth(n - 1, a.tail)
  }
}

/** Subclass for Cons and Nil, abstracti implementation */
trait List[T] {
  def isEmpty: Boolean // is the list empty?
  def head: T          // item 
  def tail: List[T]    // rest of the list
}

/** 
* Cons cell is a cell that is not empty; it contains an item. 
* Since head and tail are declared and initialized in the  class declaration 
* using val, they don't need to be declared in the class' body. In Scala, 
* val can override def, the difference between them concerns only the 
* initialization: def by name and val by value.  
*/
class Cons[T](val head: T, val tail: List[T]) extends List[T]{
  def isEmpty = false  // a Cons cell is never empty
  
  }

/** Class for empty cell */
class Nil[T] extends List[T]{
  def isEmpty = true  // a Nil cell is always empty
  def head = throw new NoSuchElementException("Nil.head") // Nil cells do not have item
  def tail = throw new NoSuchElementException("Nil.tail") // Nil cells do not have tail
  }
