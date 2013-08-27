public class BinarySearchTests{

    public static void main(String[] args){

        // Instance of binary search:
        BinarySearch binarySearch = new BinarySearch();

        // Declare some arrays:
        int[] array1 = new int[] {1, 2, 3, 4, 5, 6};
        int[] array2 = new int[] {2, 15, 17, 24, 35, 46, 57, 100, 1000, 2333};
    
        System.out.println(binarySearch.binarySearch(array1, 4));  // 3
        System.out.println(binarySearch.binarySearch(array1, 7));  // -1
        System.out.println(binarySearch.binarySearch(array2, 35)); // 4
        System.out.println(binarySearch.binarySearch(array2, 36)); // -1
    }
}