/**
* Sorts a sequence of items using merge sort, top-down implementation. 
*
* Basic plan: divide array into two halves, recursively sort each half, merge two halves. 
* Conceptually, a merge sort works as follows:
* Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is 
* considered sorted).
* Repeatedly merge sublists to produce new sublists until there is only 1 sublist remaining. 
* This will be the sorted list.
*
* Performance:
* Uses at most N lg N compares and 6 N lg N array accesses to sorty any array of size N.
* Worst case: O(n log n).
* Best case: O(n log n) typical; O(n) natural variant.
* Average case: O(n log n).
*
* Memory:
* Uses extra space proportional to N. The array aux[] needs to be of size N for the last merge.
* That means that Mergesort is not in-place, since it is  > c log N.
* You can only sort half of what you can fit in memory, the other half is used for the aux[].
*
* Practical improvements:
* 1) Mergesort has too much overhead for tiny subarrays; cutoff to insertion sort for 
* around 7 items (implemented here); this makes the algorithm around 20% faster.
* 2) Stop if already sorted. Check: is biggest item in first half <= smallest item in second
* half? Helps for partially-ordered arrays (implemented here). 
* 3) Eliminate the copy to the auxiliary array. Save time (but not space) by switching
* the role of the input and auxiliary array in each recursive call. (implemented in MergeC
* class).
*  
*
* Demo:
* You can see an animation of this algorithm in action at www.sorting-algorithms.com/merge-sort
*/
public class Merge{
    
    /**
    * Used as cutoff point at which point the insertion sort algorithm will be used instead
    * of the merge sort algorithm. Arrays of CUTOFF size will be sorted by insertion sort.
    */
    private static final int CUTOFF = 7;

    // =================================================
    //                   The Algorithm
    // =================================================
    
    /**
    * Merge algorithm.
    */
    private static void merge(Comparable[] a, Comparable[] aux, int lo, int mid, int hi){

        assert isSorted(a, lo, mid);   // precondition: a[lo..mid]   sorted
        assert isSorted(a, mid+1, hi); // precondition: a[mid+1..hi] sorted

        for (int k = lo; k <= hi; k++) // copy array a to auxiliary array aux, aux array will -
            aux[k] = a[k];             // be used to make comparisons, values will be copied -
                                       // back to array a in order
        // Merge:
        int i = lo, j = mid + 1;  // i = start of array, j = start of second half of the array
        // k = index of the array where the lesser value of the comparisons will be copied to:
        for (int k = lo; k <= hi; k++){ // for every element in the array:
            // if first half of the array is exhausted, copy all elements of the second half -
            // in current order:
            if      (i > mid)              a[k] = aux[j++]; 
            // if second half of the array is exhausted, copy all elements of the first half -
            // in current order:
            else if (j > hi)               a[k] = aux[i++];
            // copy element from second half of the array at index j if its value is less than -
            // the value of the element at the first half of the array at index i:
            else if (less(aux[j], aux[i])) a[k] = aux[j++];
            // copy element from first half of the array at index i if its value is less than -
            // the value of the element at the second half of the array at index j:
            else                           a[k] = aux[i++];
        }

        assert isSorted(a, lo, hi);  // precondition: a[lo..hi] sorted

    }
    
    /**
    * Sort algorithm, recursive routine.
    */
    private static void sort(Comparable[] a, Comparable[] aux, int lo, int hi){
        // mergesort has too much overhead for tiny subarrays; cutoff to insertion sort for 
        // around 7 items (CUTOFF constant)
        if (hi <= lo + CUTOFF - 1) Insertion.sort(a, lo, hi); // improvement 1
        int mid = lo + (hi - lo) / 2;  // computes the midpoint of the array
        sort (a, aux, lo, mid);        // sort the first half
        sort (a, aux, mid+1, hi);      // sort the second half
        merge(a, aux, lo, mid, hi);    // merge them together
    }
    
    /**
    * Sort algorithm. 
    */
    public static void sort(Comparable[] a){
        // we create the array here, because creating it in the recursive routine can lead to 
        // extensive cost of extra array creation:
        Comparable[] aux = new Comparable[a.length]; // creates the aux array
        sort(a, aux, 0, a.length -1);                // calls overloaded sort
    }
    
    // =================================================
    //                 Helper Methods
    // =================================================

    /**
    * Is v less than w?
    * @param v Item to be compared to.
    * @param w Item to be compared.
    */
    public static boolean less(Comparable v, Comparable w)
    {    return v.compareTo(w) < 0; }
    
    /**
    * Check if array is sorted? - useful for debugging.
    */
    private static boolean isSorted(Comparable[] a) {
        return isSorted(a, 0, a.length - 1);
    }
    
    /**
    * Check if array is sorted? - useful for debugging.
    */
    private static boolean isSorted(Comparable[] a, int lo, int hi) {
        for (int i = lo + 1; i <= hi; i++)
            if (less(a[i], a[i-1])) return false;
        return true;
    }
}