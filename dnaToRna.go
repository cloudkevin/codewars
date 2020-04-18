// Create a function which translates a given DNA string into RNA.

package kata

import (
	"strings"
)

func DNAtoRNA(dna string) string {
	return strings.ReplaceAll(dna, "T","U")
}