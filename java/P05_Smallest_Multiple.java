public class P05_Smallest_Multiple {
    static void swap (long a, long b) {
        long temp = a;
        a = b;
        b = temp;
    }
    static long gcd (long a, long b) {
        if (b > a) {
            swap(a, b);
        }
        if (b == 0) {
            return a;
        }
        int r = a % b;
        return gcd(b,r);
    }

    static long lcm (long a, long b) {
        return (a * b)/gcd(a,b);
    }

    public static void main (String args[]) {
        long result = 2;
        long x = 3;
        while (x <= 20) {
            result = lcm(result, x);
            x++;
        }
        System.out.println("LCM is: " + result);
    }
}
