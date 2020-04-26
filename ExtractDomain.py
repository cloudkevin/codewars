# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. 

def domain_name(url):
	print(url)
	if '//' in url:
		urlSplit = url.split('//')
		if 'www' in url:
			return urlSplit[1].split('.')[1]
		else:
			return urlSplit[1].split('/')[0].split('.')[0]
	elif 'www' in url and '//' not in url:
		return url.split('.')[1]
	else:
		return url.split('.')[0]