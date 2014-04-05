
public class FactorialLong{
    
    /** Computes n factorial using recursion. */
    public float factorialRecursive(float n){
        if (n < 1) return 1;
        return n * factorialRecursive(n - 1); 
    }
        
    /** Computes n factorial using iteration and while loop. */
    public float factorialIterW(float n){
        float acc = 1;
        while (n > 0){
            acc *= n;
            n--;
        }
        return acc;
    }
    
    /** Computes n factoral using iteration and for loop. */
    public float factorialIterF(float n){
        float acc = 1;
        for (float i = n; i > 0; i--) acc *= i;
        return acc;
    }
    
    
    
    public static void main(String[] args){
    

    }
}
