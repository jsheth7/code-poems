# By Jayesh Sheth - 2017
#
# Implement binary search in Python, includes debugging that shows inner workings & algorithmic complexity
#
# Given an input array and target value to search for, return the index of the target value in the array if found.
# If not found, return -1.
#
# Algorithmic complexity for binary search is O(log n)
# Example: if you're searching a list of 25 items, the maximum number of guesses would be log(25, 2) = 4.74.
# Rounding up, we get a maximum of 5 guesses
#
# Similarly, to search through 1 million items, it will take a maximum of 20 guesses:
# log(1000000, 2) = 19.93 . Woah!

# Try uncommenting the various options at the end. Are the number of actual guesses always different?

# Read more about binary search here:
#
# Khan Academy tutorial:
# https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array
#
# Grokking Algorithms book by Manning (recommended!)
# https://www.manning.com/books/grokking-algorithms

import math

def binary_search(input_list, sought_int):
    print "Looking for: " + str(sought_int) + " in a list with " + str(len(input_list)) + " elements"

    # 1) Let min = 0 and max = n - 1.
    min = 0
    max = len(input_list) - 1

    # If max < min, then stop: target is not present in array (empty input array). Return -1.
    if max < min:
        return -1

    # Math.floor(log2(inputArr.length) + 1);
    max_guesses = int( math.ceil( math.log( len(input_list), 2 ) ) )

    print "Maximum number of guesses: " + str(max_guesses)

    # Return an error if the element is not present in the array:
    if sought_int > input_list[max]:
        print "Value " + str(sought_int) + " was not present in the list "
        return -1

    print ""
    actual_guesses = 0

    while min <= max:
        # Find the mid point between the minimum and maximum (round down as needed)
        mid_point = int( math.floor( (min + max) / 2) )

        actual_guesses += 1
        print input_list[min:max]
        print "guess #" + str(actual_guesses) + ": " + str(input_list[mid_point])
        # print "min (index): " + str(min) + " max (index): " + str(max)
        # print "mid point index: " + str(mid_point) + " mid point value: " + str(input_list[mid_point])
        print "--------------------------------------"

        # 4) If sought value equals value at mid_point, stop - you found it!
        if input_list[mid_point] == sought_int:
            print "Actual guesses: " + str(actual_guesses)
            return mid_point

        # 5) If the guess was too low, if value at mid_point < target, then set raise the minimum by 1
        if input_list[mid_point] < sought_int:
            print "too low, look higher"
            min = mid_point + 1

        # 6) If the guess was too high, set the maximum to one below the mid point
        else:
            print "too high, look lower"
            max = mid_point - 1


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# matched_index = binary_search(primes, 5)
matched_index = binary_search(primes, 7)
# matched_index = binary_search(primes, 4)

if matched_index is not None:
    print "found!"
