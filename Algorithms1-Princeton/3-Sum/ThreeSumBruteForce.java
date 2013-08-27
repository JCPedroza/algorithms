/**
* 3-Sum algorithm, brute force approach. 
* What it does: Read in N integers and counts the number of triples that sum to exactly 0.
*
* Performance: N^3 seconds.
*
* Limitations: 1) We ignore integer overflow. 2) Doesn't handle case when input has duplicates
* (Integer overflow occurs when you try to express a number that is larger than the largest number 
* the integer type can handle.)
*/
public class ThreeSumBruteForce{
    
    /**
    * Counts how many triples sum to exactly zero. 
    * It has a triple for loop that checks if each triple i, j, k sum equals zero.
    * @param a The array of integers that will be analysed. 
    */
    public int count(int[] a){
        int N     = a.length;
        int count = 0;
        for (int i = 0; i < N; i++)
            for (int j = i + 1; j < N; j++)
                for (int k = j + 1; k < N; k++)   // Check each triple.
                    if (a[i] + a[j] + a[k] == 0)  // For simplicity, ignore integer overflow. 
                        count ++;                 // Add one to count if the triple sums zero.
        return count;
    }
}