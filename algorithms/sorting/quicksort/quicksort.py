# Based on code from Grokking Algorithms book


def quicksort(array):

    print("---------- quicksort() ---------")
    print("input array:")
    print(array)

    if len(array) < 2:
        # base case, arrays with 0 or 1 element are already "sorted"
        return array
    else:
        # recursive case

        # Take the first item in the array as the pivot
        pivot = array[0]

        print("")
        print("pivot: ")
        print(pivot)

        non_pivot_items = array[1:]

        # sub-array of all the elements less than the pivot
        # lesser_items = [i for i in array[1:] if i <= pivot]

        lesser_items = []

        for item in non_pivot_items:
            if item <= pivot:
                lesser_items.append(item)

        print("")
        print("less: ")
        print(lesser_items)

        # sub-array of all the elements greater than the pivot
        # greater_items = [i for i in array[1:] if i > pivot]
        greater_items = []

        for item in non_pivot_items:
            if item > pivot:
                greater_items.append(item)

        print("")
        print("greater: ")
        print(greater_items)

        retval = quicksort(lesser_items) + [pivot] + quicksort(greater_items)

        print("returning: ")
        print(retval)
        return retval


print quicksort([10, 5, 2, 3, 100, 34, 29, 101, 37, 1])
