// Given a year, return the century it is in.

package kata

import (
	"math"
)

func century(year int) int {
	return int(math.Ceil(float64(year)/100))
}