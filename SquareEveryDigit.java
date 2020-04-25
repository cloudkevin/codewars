public class SquareEveryDigit {

	public int squareDigits(int n) {
	String res = "";
	while (n != 0) {
		int num = n % 10;
		res = num*num + res;
		n = n/10;
	}
	return Integer.parseInt(res);
	}
}