/**
* Sorts a sequence of items using selection sort.
*
* Selection sort is a sorting algorithm, specifically an in-place comparison sort. It 
* has O(n2) time complexity, making it inefficient on large lists, and generally performs
* worse than the similar insertion sort. Selection sort is noted for its simplicity, 
* and it has performance advantages over more complicated algorithms in certain situations, 
* particularly where auxiliary memory is limited.
*
* The algorithm divides the input list into two parts: the sublist of items already sorted, 
* which is built up from left to right at the front (left) of the list, and the sublist of 
* items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist 
* is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding 
* the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging 
* it with the leftmost unsorted element (putting it in sorted order), and moving the sublist 
* boundaries one element to the right.
*
* Performance: 
* ~ N^2/2 compares and N exchanges.
* Worst, best and average case performance: O(n^2).
* Running time is insensitive to imput. It is quadratic time, even if input is sorted.
*
* Performance compared with insertion sort:
* In best case it is worse than insertion sort; quadratic instead of linear. Worst case, in 
* the other hand, is better than insertion sort. Insertion sort is: ~ 1/2 N^2 compares and 
* ~ 1/2 N^2 exchanges. They both do around the same compares, but Insertion sort does many
* more exchanges.
*
* Demo:
* You can see an animation of this sorting algorithm at www.sorting-algorithms.com/selection-sort
*/
public class Selection{
    
    /**
    * Selection sort algorithm.
    * @param a The array to be sorted.
    */
    public static void sort(Comparable[] a){
        int N = a.length;                    // length of the array
        for (int i = 0; i < N; i++){         // loops through the array
            int min = i;                     // start of unsorded portion of array
            for (int j = i + 1; j < N; j++)  // loops unsorted portion of array
                if (less(a[j], a[min]))      // finds the minimum value inside the -
                    min = j;                 // unsorted portion of the array
            exch(a, i, min);                 // swaps the minimum value with the first -
        }                                    // item in the unsorted portion of the array
    }
    
    /**
    * Is v less than w?
    * @param v Item to be compared to.
    * @param w Item to be compared.
    */
    public static boolean less(Comparable v, Comparable w)
    {    return v.compareTo(w) < 0; }
    
    /**
    * Swaps two items in an array.
    * @param i Index of item to be swaped.
    * @param j Index of item to be swaped.
    * @param a Array where the items will be swaped.
    */
    private static void exch(Comparable[] a, int i, int j){
        Comparable swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }
}