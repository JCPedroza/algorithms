
public class Factorial {
    
	/** Computes n factorial using recursion. */
	public long factorialRecursive(long n){
		if (n < 1) return 1;
		else       return n * factorialRecursive(n - 1); 
	}
	
	/** Computes n factorial using tail recursion. */
	public long factorialTailRecursive(long n){
		return tailHelper(n, 1);
	}
	private long tailHelper(long n, long acc){
		if (n < 1) return acc;
		else       return tailHelper(n - 1, acc * n);
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
