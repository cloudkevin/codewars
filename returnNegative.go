// Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
// The output should be two capital letters with a dot separating them.

package kata

import (
	"math"
)

func MakeNegative(x int) int {
	if math.Signbit(float64(x)) {
		return x
	} else {
		return x * -1
	}
}