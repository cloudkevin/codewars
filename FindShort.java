// Simple, given a string of words, return the length of the shortest word(s).

public class Kata {
	public static int findShort(String s) {
		int res = s.split(" ")[0].length();
		for (String w : s.split(" ")) {
			if (w.length() < res) {
				res = w.length();
			}
		}
		return res;
	}
}