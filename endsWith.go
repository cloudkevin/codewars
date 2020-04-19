package kata

func solution(str, ending string) bool {
	strLength, endLength := len(str), len(ending)
	if endLength > strLength {
		return false
	}
	if str[strLength-endLength:] == ending {
		return true
	} else {
		return false
	}
}