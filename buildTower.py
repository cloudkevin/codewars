# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

# Tower block is represented as *

# test.assert_equals(tower_builder(1), ['*', ])
# test.assert_equals(tower_builder(2), [' * ', '***'])
# test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****'])

import math

def tower_builder(n_floors):
	tower = []
	spaces = 0
	blocks = (n_floors*2)-1
	for n in range(n_floors):
		if n+1==n_floors and n_floors == 1:
			if n_floors == 1:
				floor = '*'
				tower.insert(0, floor)
			elif n_floors:
				floor = '  *  '
				tower.insert(0, floor)
		else:
			floor = spaces*' '+blocks*'*'+spaces*' '
			tower.insert(0, floor)
		blocks-=2
		spaces+=1
	return tower