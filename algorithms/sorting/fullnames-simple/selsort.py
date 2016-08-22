# Implementation of selection sort
#
# Based on code from Grokking Algorithms
# https://www.manning.com/books/grokking-algorithms
# It's a great book, and I highly recommend buying it!

def find_smallest(names):
    smallest = names[0]
    smallest_index = 0

    for i in range(1, len(names)):
        if names[i][0] < smallest:
            smallest = names[i][0]
            smallest_index = i

    return smallest_index

def selection_sort(names):
    sorted_list = []

    for i in range(len(names)):
        smallest = find_smallest(names)
        sorted_list.append(names.pop(smallest))

    return sorted_list