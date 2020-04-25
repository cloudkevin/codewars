//Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

public class Kata {
	public static String fakeBin(String numberString) {
		String res = "";
		for (int i=0;i<numberString.length();i++) {
			int n = Character.getNumericValue(numberString.charAt(i));
			if (n<5) {
				res+=0;
			} else if (n>=5) {
				res+=1;
			} else {
				res+=n;
			}
		}
        return res;
    }
}