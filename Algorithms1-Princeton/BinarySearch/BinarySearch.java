/**
* Solves the problem: Given a sorted array and key, find index of the key in the array.
* It's a simple algorithm, but it's very tricky to implement. First binary search was published in 1946;
* first bug-free one in 1962. Bug in Java's Arrays.binarySearch() discovered in 2006.
*
* How it works: Compare key against middle entry. If too small, go left. If too big, go right. 
* If equal, found.
*
* Performance: worst case: logbase2(N) or (lg(N)) --lg means logbase2--
*/
public class BinarySearch{
    
    /**
    * Iterative implementation of Binary Search algorithm.
    */
    public int binarySearch(int[] a, int key){
        
        // Determine highest and lowest index:
        int lo = 0;
        int hi = a.length - 1;

        while (lo <= hi){
            
            int mid = lo + (hi - lo) / 2;        // Calculate mid index.
            // 3-way compare:
            if      (key < a[mid]) hi = mid - 1; // Set a new hi point if key < mid value.
            else if (key > a[mid]) lo = mid + 1; // Set a new lo point if key > mid value.
            else return mid;                     // key = mid value, so return the index.
        }

        return -1; // Returns -1 if the key was not found
    }
        
}