//Given a list of numbers, determine whether the sum of its elements is odd or even.
//Give your answer as a string matching "odd" or "even".
//If the input array is empty consider it as: [0] (array with a zero).

public class Kata {
	public static String oddOrEven (int[] array) {
		if (array.length == 0) {
			return "even";
		}
		int total = 0;
		for (int n : array) {
			total+=n;
		}
		if (total % 2 == 0) {
			return "even";
		} else {
			return "odd";
		}
	}
}