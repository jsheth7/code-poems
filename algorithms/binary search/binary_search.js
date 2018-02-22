
/**
* By Jayesh Sheth - August, 2016
* 
* Binary search with JavaScript, including helpful debugging showing how it works and the algorithmic complexity.
* Given an input array and target value to search for, return the index of the target value in the array if found.
* If not found, return -1.
* Read more about binary search here:
* 
* Khan Academy tutorial:
* https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array
*
* Grokking Algorithms book by Manning (recommended!)
* https://www.manning.com/books/grokking-algorithms
*/

// for node, which doesn't have Math.log2() function
function log2(n) {
    return Math.log(n) / Math.log(2);
}


function binarySearch(inputArr, value){
	console.log("Looking for: " + value + " in an array with " +  inputArr.length + " elements" + "\n");
	
	// 1) Let min = 0 and max = n-1.
	var min = 0;
	var max = inputArr.length - 1;
	
	var maxGuesses = Math.floor(log2(inputArr.length) + 1);
	console.log("Number of input elements: " + inputArr.length);
	console.log("Maximum number of guesses: " + maxGuesses);
	
	
	if (value > inputArr[max]){
		console.log("value " + value + " was not present in the array " + inputArr);
		return -1;
	}
	
	var numGuesses = 0;
	
	// 2) If max < min, then stop: target is not present in array (empty input array). Return -1.
	while( min <= max ){
		// 3) Compute guess as the average of max and min, rounded down (so that it is an integer).
		var midPoint = (min + max) / 2;
		midPoint = Math.floor(midPoint);
		
		numGuesses += 1;
		
		console.log("min (index): " + min);
		console.log("max (index): " + max);
		console.log("midPoint index: " + midPoint);
		console.log("midPoint value: " + inputArr[midPoint]);
		console.log("num guesses: " + numGuesses);
		console.log("--------------------------------------");
		
		// 4) If inputArr[midPoint] equals target, then stop. You found it! Return midPoint.
		if( inputArr[midPoint] == value ){
			return midPoint;
		}
		
		// 5) If the guess was too low, that is, inputArr[midPoint] < target, then set min = midPoint + 1.
		if( inputArr[midPoint] < value ){
			console.log("Too low, look higher");
			min = midPoint + 1;
		}
		
		// 6) Otherwise, the guess was too high. Set max = guess - 1.
		else{
			console.log("Too high, look lower");
			max = midPoint - 1;
		}
		
	}
	
}

var primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97];
//var primes = [2, 3, 5, 7, 11, 13, 17, 19];

var matchedIndex = binarySearch(primes, 89);
//var matchedIndex = binarySearch(primes, 2);

console.log("matched index: " + matchedIndex);
console.log("matched value: " + primes[matchedIndex]);

