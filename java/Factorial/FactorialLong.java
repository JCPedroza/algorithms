
public class FactorialLong{
    
	/** Computes n factorial using recursion. */
	public long factorialRecursive(long n) {
		if (n < 1) return 1;
		return n * factorialRecursive(n - 1); 
	}

	/** Computes n factorial using tail recursion. */
    public long factorialTailRecursive(long n) {
        return factorialTailRecursiveLoop(n, 1);
    }
    public long factorialTailRecursiveLoop(long n, long acc) {
    	if (n < 1) return acc;
    	return factorialTailRecursiveLoop(n - 1, n * acc);
    }
		
	/** Computes n factorial using iteration and while loop. */
	public long factorialIterW(long n) {
		long acc = 1;
		while (n > 0) {
			acc *= n;
			n--;
		}
		return acc;
	}
	
	/** Computes n factoral using iteration and for loop. */
	public long factorialIterF(long n) {
		long acc = 1;
		for (long i = n; i > 0; i--) acc *= i;
		return acc;
	}
	
	
	public static void main(String[] args) {
	    FactorialLong Factorial = new FactorialLong();
		int  num     = 25;
		long repeats = 10000000;
		long start   = 0;
		long end     = 0;
		long total   = 0;
		String string = String.format("Execution time for %d factorial, %d repetitions:", num, repeats);

        System.out.println(string);

        start = System.nanoTime();
	    for (int i = 0; i < repeats; i++) {
	    	Factorial.factorialRecursive(num);
	    }
	    end = System.nanoTime();
	    total = (end - start) / 1000000;
        System.out.println(String.format("recursive: %d", total));

        start = System.nanoTime();
	    for (int i = 0; i < repeats; i++) {
	    	Factorial.factorialTailRecursive(num);
	    }
	    end = System.nanoTime();
	    total = (end - start) / 1000000;
        System.out.println(String.format("tail recursive: %d", total));
        
        start = System.nanoTime();
	    for (int i = 0; i < repeats; i++) {
	    	Factorial.factorialIterW(num);
	    }
	    end = System.nanoTime();
	    total = (end - start) / 1000000;
        System.out.println(String.format("while: %d", total));

        start = System.nanoTime();
	    for (int i = 0; i < repeats; i++) {
	    	Factorial.factorialIterF(num);
	    }
	    end = System.nanoTime();
	    total = (end - start) / 1000000;
        System.out.println(String.format("for: %d", total));

	}
}
