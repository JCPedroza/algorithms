import java.util.Arrays;

public class Test{

    public static void main(String[] args){

        Integer[] intArray1 = new Integer[] {5, 2, 1, 4, 3};
        Integer[] intArray2 = new Integer[] {5, 2, 1, 4, 3};
        
        Selection.sort(intArray1);
        System.out.println(Arrays.toString(intArray1));
        Insertion.sort(intArray2);
        System.out.println(Arrays.toString(intArray2));
    }
}