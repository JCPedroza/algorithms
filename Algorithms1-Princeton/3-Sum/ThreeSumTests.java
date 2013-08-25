public class ThreeSumTests{

    public static void main(String[] args){
        
        // References
        ThreeSumBruteForce TSBF = new ThreeSumBruteForce();

        // Arrays to use for tests
        int[] array1 = new int[] {1, -2, 1, 1}; // 3
        int[] array2 = new int[] {3, 4, 5, 6};  // 0

        // Prints

        // Brute force approach:
        System.out.println(TSBF.count(array1));
        System.out.println(TSBF.count(array2));

    }
}