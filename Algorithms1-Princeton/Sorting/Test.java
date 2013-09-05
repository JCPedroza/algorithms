import java.util.Arrays;

public class Test{

    public static void main(String[] args){

        Integer[] intArray1 = new Integer[] {1, 2, 3, 4};
        
        Selection.sort(intArray1);
        System.out.println(Arrays.toString(intArray1));
    }
}