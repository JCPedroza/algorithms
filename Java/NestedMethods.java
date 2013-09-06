/**
* How expensive is to nest overloaded methods? It improves readability, 
* and helps us to don't repear ourselves; but is it worth it?
*
* To compile: javac NestedMethods.java
* To run: java NestedMethods arraysize numberoftests
* Example: to run 100 tests on an array of size 1000:
* java NestedMethods 1000 100
*/
public class NestedMethods{
    
    /**
    * Iterates through an array of ints, counts iterations, returns the count.
    */
    public int method1(int[] anArray){
        int count = 0;
        for(int e = 0; e < anArray.length; e++)
            count ++;
        return count;
    }

    /**
    * Iterates through an array of ints, counts iterations, returns the count.
    * Calls method1(int[] anArray) to do the work. 
    */
    public int method1(int[] anArray, int dummyInt){
        return method1(anArray);
    }

    public static void main(String[] args){
        
        // ===================================
        // Variable and reference declaration
        // ===================================

        long          startTime;
        long          duration1;
        long          duration2;
        long          average1;
        long          average2;
        int           arraySize     = Integer.parseInt(args[0]);
        int           numberOfTests = Integer.parseInt(args[1]);
        NestedMethods nestedMethods = new NestedMethods();
        int[]         intArray      = new int[arraySize];

        // ===================================
        // Perform tests
        // ===================================
        
        // Without nested method:
        startTime = System.nanoTime();
        for (int i = 0; i < numberOfTests; i++){
            nestedMethods.method1(intArray);
        }
        duration1 = System.nanoTime() - startTime;
        average1  = duration1 / numberOfTests;

        // With nested method:
        startTime = System.nanoTime();
        for (int i = 0; i < numberOfTests; i++){
            nestedMethods.method1(intArray, 0);
        }
        duration2 = System.nanoTime() - startTime;
        average2  = duration2 / numberOfTests;
        
        // ===================================
        // Prints:
        // ===================================

        System.out.println("");
        System.out.println("Performed " + numberOfTests + " tests with an array of size " + arraySize);
        System.out.println("All times in nanoseconds.");
        System.out.println("");
        System.out.println("Results without nested method: ");
        System.out.println("Total: " + duration1 + " Average: " + average1);
        System.out.println("");
        System.out.println("Results with nested method: ");
        System.out.println("Total: " + duration2 + " Average: " + average2);
        System.out.println("");


    }
}