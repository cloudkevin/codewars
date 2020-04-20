// The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz 
// (ignore the last chunk if its size is less than sz).
// If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; 
// otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.
// If
// sz is <= 0 or if str is empty return ""
// sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".

package kata

import (
	"math"
)

func Revrot(s string, n int) string {
	if n <= 0 || n > len(s) {
		return ""
	}
	newValue := ""
	chunk := s[0:len(s)-len(s)%n]
	numGroups, count, start, end := len(chunk)/n, 0, 0, n
	for count < numGroups {
		curRange := chunk[start:end]
		total := 0
		for _, z := range curRange {
			total +=  int(math.Pow(float64(int(z - '0')), 3))
		}
		if total % 2 == 0 {
			newValue += string(Reverse(curRange))
		} else {
			newValue += string(curRange[1:]+curRange[0:1])
		}
		count+=1
		start += n
		end += n
	}

	return newValue
}

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}