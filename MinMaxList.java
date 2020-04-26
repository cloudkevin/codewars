// Your task is to make two functions, max and min (maximum and minimum in PHP and Python) that take a(n) array/vector of integers list as input and outputs, respectively,
// the largest and lowest number in that array/vector.

import java.util.Arrays;
import java.util.Collections;

public class Kata {
	public static int min(int[] list) {
		Arrays.sort(list);
		return list[0];
	}
	
	public static int max(int[] list) {
		Arrays.sort(list);
		return list[list.length-1];
	}
}