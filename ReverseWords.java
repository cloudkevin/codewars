// Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

public class Kata {
	public static String reverseWords(final String original) {
		if (original.trim().length() == 0) {
			return original;
		}
		String words[]=original.split(" "); 
		String res = "";
		for (String w: words) {
			StringBuilder sb=new StringBuilder(w);
			sb.reverse();
			res+=sb.toString()+" "; 
			
		}
		return res.trim();
	}
}