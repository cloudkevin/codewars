// Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side)

package kata

func DirReduc(arr []string) []string {
	if len(arr) == 0 {
		return []string{}
	}

	reducArr := []string{}

	for i := len(arr) - 1; i > 0; i-- {
		if (arr[i] == "NORTH" && arr[i-1] == "SOUTH") ||
			 (arr[i] == "SOUTH" && arr[i-1] == "NORTH") ||
			 (arr[i] == "EAST" && arr[i-1] == "WEST") ||
			 (arr[i] == "WEST" && arr[i-1] == "EAST") {
			reducArr = append(reducArr, arr[:i-1]...)
			reducArr = append(reducArr, arr[i+1:]...)
			return DirReduc(reducArr)
		}
	}
	return arr
}