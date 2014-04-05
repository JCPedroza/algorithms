
public class FactorialLong{
    
	/** Computes n factorial using recursion. */
	public long factorialRecursive(long n){
		if (n < 1) return 1;
		return n * factorialRecursive(n - 1); 
	}
		
	/** Computes n factorial using iteration and while loop. */
	public long factorialIterW(long n){
		long acc = 1;
		while (n > 0){
			acc *= n;
			n--;
		}
		return acc;
	}
	
	/** Computes n factoral using iteration and for loop. */
	public long factorialIterF(long n){
		long acc = 1;
		for (long i = n; i > 0; i--) acc *= i;
		return acc;
	}
	
	
	
	public static void main(String[] args){
		
	}
}
