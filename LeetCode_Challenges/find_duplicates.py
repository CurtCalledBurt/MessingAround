# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.


def find_duplicates(array):
    # function that scans an array for duplicates that returns True if it contains duplicates and False if it does not. Also returns a dictionary with the duplicate elements of the array as keys and the total count of those duplicates in the original array as values. Duplicate-Count pairs.


    # we don't know the addresses of any of these elements, so to search for a duplicate of any of them would be an O(n) operation, doing that for every element in the array would then be an O(n**2) operation. We are going to convert this array to a set, an O(n) operation, in order to achieve an O(1) look up time, giving a total O(n) operation time.
    ht = set()
    duplicates = {}
    # store every element in the hashtable
    for elem in array:
        # add elem to duplicates if it already exists in ht
        if elem in ht:
            if elem not in duplicates:
                # when counting duplicates, we start at 2, because any duplicate occurs twice!
                duplicates[elem] = 2
            else:
                duplicates[elem] += 1
        ht.add(elem)

    return (len(duplicates) > 0), duplicates


# Testing find_duplicates
array = [1,2,3,4,5,6,7,8,9,1,1,1,1,1]
print(find_duplicates(array))

array = [1,2,3,4,5]
print(find_duplicates(array))

array = [1,2,3,4,5,6,7,8,9,1]
print(find_duplicates(array))

array = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,9,2,3,4,10]
print(find_duplicates(array))