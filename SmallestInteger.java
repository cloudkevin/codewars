// Given an array of integers your solution should find the smallest integer.

public class Kata {
	public static int findSmallestInt(int[] args) {
		int smallest = args[0];
		for (int i=0;i<args.length;i++) {
			if(args[i] < smallest) {
				smallest = args[i];
			}
		}
		return smallest;
	}
}