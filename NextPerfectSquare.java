// Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter

import java.lang.Math;

public class Kata {
	public static long findNextSquare(long sq) {
		double d = (double)sq;
		double square = Math.sqrt(d);
		if((square - Math.floor(square)) != 0) {	
			return -1;
		}
		d+=1;
		sq+=1;
		square=Math.sqrt(d);
		while ((square - Math.floor(square)) != 0) {
			d+=1;
			sq+=1;
			square=Math.sqrt(d);
		}
		return sq;
	}
}