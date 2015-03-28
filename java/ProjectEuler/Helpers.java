
public class Helpers {
    
    public static boolean isPrimeTrialDivision(long n) {
        if (n < 2) {
            return false;
        }
        if (n < 4) {
            return true;
        }
        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }

        long limit = (long) Math.sqrt(n);
        int divisor = 5;

        while (divisor <= limit) {
            if (n % divisor == 0 || n % (divisor + 2) == 0) {
                return false;
            }
            divisor += 6;
        }

        return true;
    }
}