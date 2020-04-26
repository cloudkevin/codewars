// Your task is to write a function which returns the sum of following series upto nth term(parameter).
// Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

public class Kata {
	public static String seriesSum(int n) {
		float total = 1;
		int divisor = 4;
		for(int i=1;i<n;i++) {
			total+= ((float) 1) / divisor;
			divisor += 3;
		}
		return String.format ("%.2f", total);
	}
}