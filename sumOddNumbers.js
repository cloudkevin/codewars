// Given the triangle of consecutive odd numbers calculate the row sums of this triangle from the row index (starting at index 1)
//              1
//           3     5
//        7     9    11
//    13    15    17    19
// 21    23    25    27    29

function rowSumOddNumbers(n) {
	let startNum = (n*n) - (n-1);
	let c = 0;
	let res = 0;
	while (c < n) {
		if (startNum % 2 !== 0) {
			res += startNum;
			c++;
		}
		startNum++;
	}
	return res;
}