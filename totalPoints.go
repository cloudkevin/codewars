// Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.

// For example: ["3:1", "2:2", "0:1", ...]

// Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:

// if x>y - 3 points
// if x<y - 0 point
// if x=y - 1 point

package kata

import (
	"strings"
)

func Points(games []string) int {
	score := 0
	for _, game := range games {
		split := strings.Split(game, ":")
		if split[0] > split[1] {
			score += 3
		} else if split[0] == split[1] {
			score += 1
		}
	}
	return score
}