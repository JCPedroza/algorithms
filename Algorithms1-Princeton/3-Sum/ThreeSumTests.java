import java.lang.reflect.Method; // used for reflection, to use methods as parameters

/**
* Class with the main method, used to perform tests on the 3-sum algorithms
*/
public class ThreeSumTests{
    
    // ==========
    // Helpers
    // ==========

    /**
    * Performs several runs of the algorithms, measuring time and calculating average.
    * Times will be not exact because of the method.invoke() call.
    * @param arrayOfArrays An array that contains arrays that will be used to perform 
    * the tests.
    * @param mode 1 to run brute force approac, 2 (or any other value ;) )to run binary search approach.
    * @return Average running time.
    */
    private static long runningTime(int[][] arrayOfArrays, int mode) throws Exception{

        final int    arrayLength     = arrayOfArrays.length;
        final Method bruteAlgorithm  = ThreeSumBruteForce.class.getMethod("count", int.class);
        final Method binaryAlgorithm = ThreeSumBinarySearch.class.getMethod("count", int.class);
              long   sum             = 0;
        
        // Test brute force approach (mode = 1).
        if (mode == 1){    
            for (int i = 0; i < arrayLength; i++){
                long startTime = System.nanoTime();
                bruteAlgorithm.invoke(new Object(), arrayOfArrays[i]);
                long stopTime  = System.nanoTime();
                sum += stopTime - startTime;
            }
            
        }
        
        // Test binary search approach (mode = 2, or anyting else actually).
        else{
            for (int i = 0; i < arrayLength; i++){
                long startTime = System.nanoTime();
                binaryAlgorithm.invoke(new Object(), arrayOfArrays[i]);
                long stopTime  = System.nanoTime();
                sum += stopTime - startTime;
            }
        }
        
        // Return average time.
        return sum / arrayLength;
    }

    /**
    * Generates an array of random numbers
    * @param size Size of the array to be generated.
    * @param min  Minimum value.
    * @param max  Maximum value.
    * @return An array of random numbers
    */
    private static int[] makeRandomArray(int size, int min, int max){
        int[] returnArray = new int[size];
        for (int i = 0; i < size; i++) {
            returnArray[i] = (int) (Math.random() * (max - min + 1)) + min;
        }
        return returnArray;
    }

    
    // ==========
    // main()
    // ==========

    public static void main(String[] args){
        
        // ==========
        // Instances
        // ==========

        ThreeSumBruteForce   TSBF = new ThreeSumBruteForce();
        ThreeSumBinarySearch TSBS = new ThreeSumBinarySearch();

        // ==========
        // Arrays
        // ==========

        int[] array1 = new int[] {1, -2, 3, -3, -1, 4, -4, 5, -5}; 
        int[] array2 = new int[] {3, 4, 5, 6};  

        // ==========
        // Prints
        // ==========

        // Brute force approach, checking everything is ok:
        // System.out.println(TSBF.count(array1)); // 6
        // System.out.println(TSBF.count(array2)); // 0

        // Binary search approach, checking everything is ok:
        // System.out.println(TSBS.count(array1)); // 6
        // System.out.println(TSBS.count(array2)); // 0
    }
}