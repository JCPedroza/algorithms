import java.util.Arrays;

public class Test{

    public static void main(String[] args){
        
        Integer[] intArray0 = new Integer[] {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        Integer[] intArray1 = new Integer[] {5, 2, 1, 4, 3, 10, 9, 8, 20, 18, -5, -100, 23, -15};
        Integer[] intArray2 = new Integer[] {5, 2, 1, 4, 3, 10, 9, 8, 20, 18, -5, -100, 23, -15};
        Integer[] intArray3 = new Integer[] {5, 2, 1, 4, 3, 10, 9, 8, 20, 18, -5, -100, 23, -15};

        Selection.sort(intArray1);
        System.out.println(Arrays.toString(intArray1));
        Insertion.sort(intArray2);
        System.out.println(Arrays.toString(intArray2));
        Shell.sort(intArray3);
        System.out.println(Arrays.toString(intArray3));
        for (int e = 0; e < 10; e++){
            KnuthShuffle.shuffle(intArray0);
            System.out.println(Arrays.toString(intArray0));
        }

    }
}