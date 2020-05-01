// An isogram is a word that has no repeating letters, consecutive or non-consecutive.
// Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.
// Ignore letter case.

import java.util.Arrays;

public static boolean  isIsogram(String str) {
		str = str.toLowerCase();
		int len = str.length();
		if (len == 0) {
			return true;
		}
		char arr[] = str.toCharArray();
		Arrays.sort(arr);
		for (int i=0;i<len-1;i++) {
			if(arr[i] == arr[i+1]) {
				return false;
			}
		}
		return true;
		}