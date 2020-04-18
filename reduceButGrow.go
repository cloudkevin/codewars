// Given a non-empty array of integers, return the result of multiplying the values together in order.

package kata

func Grow(arr []int) int{
	total := arr[0]
	for _, n := range arr[1:] {
		total = total * n
	}
	return total
}