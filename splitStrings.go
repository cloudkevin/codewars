// Complete the solution so that it splits the string into pairs of two characters. 
// If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

package kata

func Solution(str string) []string {
	res := []string{}
	for len(str) > 0 {
		if len(str) != 0 {
			if len(str) > 1 {
				res = append(res, str[0:2])
				str = str[2:]
			} else if len(str) == 1 {
				res = append(res, str[0:1]+"_")
				str = str[1:]
			}
		}
	}
	return res
}