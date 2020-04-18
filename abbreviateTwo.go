// Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
// The output should be two capital letters with a dot separating them.

package kata

import (
	"strings"
	"fmt"
)

func AbbrevName(name string) string{
	fn, ln := strings.Split(name, " ")[0], strings.Split(name, " ")[1]
	return fmt.Sprintf("%s.%s", strings.ToUpper(fn[:1]), strings.ToUpper(ln[:1]))
}