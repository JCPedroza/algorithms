/**
* Solves the problem: Given a sorted array and key, find index of the key in the array.
* It's a simple algorithm, but it's very tricky to implement. First binary search was published in 1946;
* first bug-free one in 1962. Bug in Java's Arrays.binarySearch() discovered in 2006.
*
* How it works: 
* the algorithm compares the search key value with the key value of the middle element of the array. 
* If the keys match, then a matching element has been found and its index, or position, is returned. 
* Otherwise, if the search key is less than the middle element's key, then the algorithm repeats its 
* action on the sub-array to the left of the middle element or, if the search key is greater, on the 
* sub-array to the right. If the remaining array to be searched is empty, then the key cannot be 
* found in the array and a special "not found" indication is returned.
*
* Performance: 
* Worst case:   O(log n)
* Best case:    O(1)
* Average case: O(log n)
*/
object BinarySearch{

  /**
  * Recursive implementation of Binary Search algorithm.
  */
  def binarySearch(arr: Array[Int], key: Int) = {

    def recursion(lo: Int, hi: Int): Int = {
      if (lo > hi) -1                                   // base case, key not found: return -1
      else{
        var mid = lo + (hi - lo) / 2                    // calculate middle index
        // 3-way compare:
        if      (key < arr(mid)) recursion(lo, mid - 1) // set a new hi point if key < mid value
        else if (key > arr(mid)) recursion(mid + 1, hi) // set a new lo point if key > mid value
        else mid                                        // key = mid, return that index
      }
    }
    
    // first recursion call, lo is the start of the array, hi is the end 
    recursion(0, arr.length - 1)
  }
}