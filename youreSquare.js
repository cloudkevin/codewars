// Given an integral number, determine if it's a square number

var isSquare = function(n){
	if(n==0){return true;}
	return n > 0 && Math.sqrt(n) % 1 === 0;
}