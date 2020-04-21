// This time no story, no theory. The examples below show you how to write function accum:
// accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

function accum(s) {
	res = []
	for (var i = 0; i < s.length; i++) {
		res.push(s[i].charAt(0).toUpperCase()+s[i].repeat(i).toLowerCase())
	}
	return res.join('-')
}