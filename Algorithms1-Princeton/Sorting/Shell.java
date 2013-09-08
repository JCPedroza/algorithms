public class Shell{
    
    /**
    * Shell sort algorithm.
    * @param a The array to be sorted.
    */
    public static void sort(Comparable[] a){
        int N = a.length;
        int h = 1;
        while(h < N / 3) h = 3*h + 1;   // 3x+1 increment sequence: 1, 4, 13, 40, 121...
        while(h >= 1){                  // sort the array
            for(int i = h; i < N; i++){
                // insertion sort:
                for(int j = i; j >= h && less(a[j], a[j - h]); j-= h)
                    exch(a, j, j - h);
            } 
            h = h / 3;
        }                              // move to next increment
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