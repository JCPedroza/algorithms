import java.util.*;

/**
* Testing running time of iteration dynamics against recursion dynamics in Java.
* To compile: javac IterationVsRecursion.java
* To run: java IterationVsRecursion numberOfTests depthOfTests
* To run example: java IterationVsRecursion 100 100 will perform 100 tests on each
* Warning: depth must be less than 1958 or a stack overflow exception will be thrown.
* algorithm, each algorithm will be called with a parameter of 100.
*/
public class IterationVsRecursion{

    // =======================================
    // Dynamic 1: Populating an array.
    // =======================================

    // Populating an array with recursion:
    private int[] recursiveBuilder(int depth, int[] anArray){
        // Base case:
        if (depth <= 0) return anArray;
        // Recursion:
        else{
            depth--;
            anArray[depth] = depth;
            return recursiveBuilder(depth, anArray);
        }
    }
    private int[] recursiveBuilder(int depth){
        return recursiveBuilder(depth, new int[depth]);
    }

    // Populating an array with iteration:
    private int[] iterativeBuilder(int depth){
        int[] returnArray = new int[depth]; 
        for (int i = 0; i < depth; i++) returnArray[i] = i;
        return returnArray;
    }

    // =======================================
    // Dynamic 2: Simple loops.
    // =======================================
    
    // Simple recursive loop
    private int recursiveLoop(int depth){
        if (depth <= 0) return 0;
        else {
            depth--;
            return recursiveLoop(depth);
        }
    }

    //Simple iterative loop
    private int iterativeLoop(int depth){
        for (int i = 0; i < depth;){i++;}
        return 0;
    }

    // =======================================
    // main(), tests, and prints:
    // =======================================

    public static void main(String[] args){
        IterationVsRecursion ivsr = new IterationVsRecursion();
        
        int times = Integer.parseInt(args[0]);
        int depth = Integer.parseInt(args[1]);
        
        //============
        // Dynamic 1.
        //============

        // measure recursive implementation.
        long startTime = System.nanoTime();
        for (int i = 0; i < times; i++) ivsr.recursiveBuilder(depth);
        long   endTime    = System.nanoTime();
        long duration1R = (endTime - startTime);
        long average1R  = duration1R / times;
        // measure iterative implementation.
        startTime = System.nanoTime();
        for (int i = 0; i < times; i++) ivsr.iterativeBuilder(depth);
        endTime    = System.nanoTime();
        long duration1I = (endTime - startTime);
        long average1I  = duration1I / times;

        //============
        // Dynamic 2.
        //============

        // measure recursive implementation.
        startTime = System.nanoTime();
        for (int i = 0; i < times; i++) ivsr.recursiveLoop(depth);
        endTime    = System.nanoTime();
        long duration2R = (endTime - startTime);
        long average2R  = duration2R / times;
        // measure iterative implementation.
        startTime = System.nanoTime();
        for (int i = 0; i < times; i++) ivsr.iterativeLoop(depth);
        endTime    = System.nanoTime();
        long duration2I = (endTime - startTime);
        long average2I  = duration2I / times;
        
        //============
        // Prints.
        //============

        System.out.println("");
        System.out.println("Performing " + times + " tests with depth " + depth +":");
        System.out.println("");

        // dynamic 1 recursive
        System.out.print("Dynamic 1 recursive: ");
        System.out.println("total: " + duration1R + " average: " + average1R);
        // dynamic 1 iterative
        System.out.print("Dynamic 1 iterative: ");
        System.out.println("total: " + duration1I + " average: " + average1I);
        System.out.println("");

         // dynamic 2 recursive
        System.out.print("Dynamic 2 recursive: ");
        System.out.println("total: " + duration2R + " average: " + average2R);
        // dynamic 2 iterative
        System.out.print("Dynamic 2 iterative: ");
        System.out.println("total: " + duration2I + " average: " + average2I);
        System.out.println("");


    }

}