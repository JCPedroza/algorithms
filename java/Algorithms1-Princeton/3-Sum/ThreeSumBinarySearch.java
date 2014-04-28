import java.util.Arrays;

/**
* 3-Sum algorithm Binary Searc approach.
* What it does: Read in N integers and counts the number of triples that sum to exactly 0.
* Faster implementation of the 3-sum algorithm that uses binary search instead of brute force.
* The array to be scanned needs to be sorted first. 
* 
* Performance: N^2 log N. Brute Force performance is: N^3. The improvement in performance is big.
*
* Limitations: 1) We ignore integer overflow. 2) Doesn't handle case when input has duplicates
* (Integer overflow occurs when you try to express a number that is larger than the largest number 
* the integer type can handle.)
*/
public class ThreeSumBinarySearch{
    
    public int count(int[] a){

        int N = a.length;
        int count = 0;

        Arrays.sort(a); // Array needs to be sorted.
        
        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                int k = Arrays.binarySearch(a, -(a[i] + a[j])); // Implementation of binary search
                if (k > j){
                    count++;
                }
            }
        }
        return count;
    }
}