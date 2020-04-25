// Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

public class Kata {
	public static boolean getXO (String str) {
		char[] chars = str.toLowerCase().toCharArray();
		int x = 0;
		int y = 0;
		for (char c: chars) { 
			switch(c) {
			case 'x':
				x += 1;
				break;
			case 'o':
				y += 1;
				break;
			}
		}
		if (x==y) {
			return true;
		} else {
			return false;
		}
	}
}