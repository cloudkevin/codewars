// Complete the square sum function so that it squares each number passed into it and then sums the results together.

#include <stddef.h>

int square_sum(const int *values, size_t count){
	int res = 0;
	for (int x = 0; x < count; x++)
		res += values[x]*values[x];
	return (res);
}