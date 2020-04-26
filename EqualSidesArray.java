// You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal
// to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

//sloppy implementation

public static int findEvenIndex(int[] arr) {
		int index = -1;
		int sumTotal=0;
        for (int i=0; i < arr.length; i++){
            sumTotal += arr[i];
        }
		if (sumTotal - arr[0] == 0) {
			return 0;
		}
		for (int i = 1; i < arr.length; i ++) {
			int left = 0;
			int right = 0;
			for (int j = 0; j < i; j ++) {
				left = left + arr[j];
			}
			for (int k = i + 1; k < arr.length; k ++) {
				right = right + arr[k];
			}
			if (left == right) {
				index = i;
			}
		}
		return index;
	}