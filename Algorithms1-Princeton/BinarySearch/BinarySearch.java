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