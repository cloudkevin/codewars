// Given a positive integer n, calculate the following sum:
// n + n/2 + n/4 + n/8 + ...

public class Kata {
	public static int halvingSum(int n) {
		int d = 2;
		int res = n;
		while (d <= n) {
			res += n/d;
			d*=2;
		}
		return res;
	}
}