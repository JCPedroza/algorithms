public class ThreeSumTests{

    public static void main(String[] args){
        
        // References
        ThreeSumBruteForce   TSBF = new ThreeSumBruteForce();
        ThreeSumBinarySearch TSBS = new ThreeSumBinarySearch();

        // Arrays to use for tests
        int[] array1 = new int[] {1, -2, 3, -3, -1, 4, -4, 5, -5}; 
        int[] array2 = new int[] {3, 4, 5, 6};  

        // Prints

        // Brute force approach:
        System.out.println(TSBF.count(array1)); // 6
        System.out.println(TSBF.count(array2)); // 0

        // Binary search approach:
        System.out.println(TSBS.count(array1)); // 6
        System.out.println(TSBS.count(array2)); // 0
    }
}