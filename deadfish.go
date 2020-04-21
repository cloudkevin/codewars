// Write a simple parser that will parse and run Deadfish.

// Deadfish has 4 commands, each 1 character long:

// i increments the value (initially 0)
// d decrements the value
// s squares the value
// o outputs the value into the return array
// Invalid characters should be ignored.

package kata

func Parse(data string) []int{
	start, end, value := 0, 1, 0
	response := []int{}
	for end <= len(data) {
		char := data[start:end]
		switch char {
		case "i":
			value += 1
		case "d":
			value -=1
		case "s":
			value = value*value
		case "o":
			response = append(response, value)
		}
		start += 1
		end += 1
	}
	return response
}