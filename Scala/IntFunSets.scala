/**
* Purely functional sets of integers. 
*
* Representation:
* 
* As an example to motivate our representation, how would you represent the set of all negative 
* integers? You cannot list them all… one way would be so say: if you give me an integer, I can 
* tell you whether it’s in the set or not: for 3, I say no; for -1, I say yes.
*
* Mathematically, we call the function which takes an integer as argument and which returns a 
* boolean indicating whether the given integer belongs to a set, the characteristic function of 
* the set. For example, we can characterize the set of negative integers by the characteristic 
* function (x: Int) => x < 0.
*
* Therefore, we choose to represent a set by its characterisitc function and define a type alias 
* for this representation:
* type Set = Int => Boolean
* Using this representation, we define a function that tests for the presence of a value in a set:
* def contains(s: Set, elem: Int): Boolean = s(elem)
*
* In order to limit the search space, we set the range of forall and exists to a bound value; the 
* scan will be made from -bound to bound (from -1000 to 1000 if bound = 1000).
*/
object IntFunSets {
  /**
  * We represent a set by its characteristic function, i.e.
  * its `contains` predicate.
  */
  type Set = Int => Boolean

  /**
  * Indicates whether a set contains a given element.
  */
  def contains(s: Set, elem: Int): Boolean = s(elem)

  /**
  * Returns the set of the one given element.
  */
  def singletonSet(elem: Int): Set = 
    x => x == elem

  /**
  * Returns the union of the two given sets,
  * the sets of all elements that are in either `s` or `t`.
  */
  def union(s: Set, t: Set): Set = 
    x => s(x) || t(x)

  /**
  * Returns the intersection of the two given sets,
  * the set of all elements that are both in `s` and `t`.
  */
  def intersect(s: Set, t: Set): Set =
    x => s(x) && t(x)

  /**
  * Returns the difference of the two given sets,
  * the set of all elements of `s` that are not in `t`.
  */
  def diff(s: Set, t: Set): Set =
    x => s(x) && !t(x)

  /**
  * Returns the subset of `s` for which `p` holds.
  */
  def filter(s: Set, p: Int => Boolean): Set = 
    intersect(s, p)

  /**
  * The bounds for `forall` and `exists` are +/- 1000, 
  * in order to limit the search space.
  */
  val bound = 1000

  /**
  * Returns whether all bounded integers within `s` satisfy `p`.
  */
  def forall(s: Set, p: Int => Boolean): Boolean = {
    def iter(a: Int): Boolean = {
      if (a > bound) true
      else if (s(a) && !p(a)) false 
      else iter(a + 1)
    }
    iter(-bound)
  }

  /**
  * Returns whether there exists a bounded integer within `s`
  * that satisfies `p`.
  */
  def exists(s: Set, p: Int => Boolean): Boolean = 
    !forall(s, x => !p(x))

  /**
  * Returns a set transformed by applying `f` to each element of `s`.
  */
  def map(s: Set, f: Int => Int): Set =
    y => exists(s, x => y == f(x))

  /**
  * Displays the contents of a set
  */
  def toString(s: Set): String = {
    val xs = for (i <- -bound to bound if contains(s, i)) yield i
    xs.mkString("{", ",", "}")
  }

  /**
  * Prints the contents of a set on the console.
  */
  def printSet(s: Set) {
    println(toString(s))
  }
}