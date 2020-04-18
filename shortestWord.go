// Simple, given a string of words, return the length of the shortest word(s).

package kata

import (
	"strings"
)

func FindShort(s string) int {
	length := len(strings.Split(s," ")[0])
	for _, word := range strings.Split(s, " ") {
		if len(word) < length {
			length = len(word)
		}
	}
	return length
}