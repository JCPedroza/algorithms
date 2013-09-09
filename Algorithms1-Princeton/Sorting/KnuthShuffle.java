/**
* Shuffles a sequence of items using knuth shuffle.
*
* It is similar to insertion sort, but the swap is between a[i] and a random index between
* 0 and i. In iteration i, pick integer r between 0 and 9 uniformly at random; then swap
* a[i] and a[r].
*
* Knuth shuffling algorithm produces a uniformly random permulation (assuming integers
* uniformly at random) of the input array in linear time.
*
* Performance: 
* O(n) (linear). 
*/
public class KnuthShuffle{
    
    /**
    * Knuth shuffle algorithm.
    * @param a The array to be shuffled. 
    */ 
    public static void shuffle(Comparable[] a){
        int N = a.length;            // length of the array
        for (int i = 0; i < N; i++){ // loop through the array
            int r = random(i);       // generate random number between 0 and i (inclusive)
            exch(a, i, r);           // swap i with that random index between 0 and i
        }
    }

    /**
    * Produces a random integer between 0 and range (inclusive).
    * @param range Range of the random number generation.
    * @return A random integer between 0 and range.
    */
    private static int random(int range){
        return (int)(Math.random() * (range + 1));
    }

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