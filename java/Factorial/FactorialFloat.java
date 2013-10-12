
public class FactorialLong{
    
    /** Computes n factorial using recursion. */
    public float factorialRecursive(float n){
        if (n < 1) return 1;
        else       return n * factorialRecursive(n - 1); 
    }
    
    /** Computes n factorial using tail recursion. */
    public float factorialTailRecursive(float n){
        return tailHelper(n, 1);
    }
    private float tailHelper(float n, float acc){
        if (n < 1) return acc;
        else       return tailHelper(n - 1, acc * n);
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
        Factorial f = new Factorial();
        
        System.out.println(f.factorialRecursive(4));
        System.out.println(f.factorialRecursive(5));
        System.out.println(f.factorialTailRecursive(4));
        System.out.println(f.factorialTailRecursive(5));
        System.out.println(f.factorialIterF(4));
        System.out.println(f.factorialIterF(5));
        System.out.println(f.factorialIterW(4));
        System.out.println(f.factorialIterW(5));
    }
}
