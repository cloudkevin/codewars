// Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

function songDecoder(song) {
	return song.split('WUB').join(' ').replace(/ +(?= )/g,'').trim()
}