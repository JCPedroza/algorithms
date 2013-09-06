public class Insertion{
    
    /**
    * Insertion sort algorithm.
    * @param a The array to be sorted.
    */
    public static void sort(Comparable[] a){
        int N = a.length;                  // length of the array
        for (int i = 0; i < N; i++)        // loop through the array
            for (int j = i; j > 0; j--)    // loop through the sorted portion of array
                if (less(a[j], a[j - 1]))  // if the value to the left is >= a[j]:
                    exch(a, j, j - 1);     // swap the items in the array
                else break;                // break the loop if the value to the left -
    }                                      // is <= a[j]        

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