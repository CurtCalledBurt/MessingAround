# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def find_sum(array, target):
    ht = {}
    # add elements of array to dictionary in element-index pairs
    for i in range(len(array)):
        ht[array[i]] = i
    
    # for each element in the array, check if target - element is in the dictionary. If this is the case, it means we have a valid sum and we return the index of the elements
    for elem in array:
        needed = target - elem
        if needed in ht.keys():
            return [ht[elem], ht[needed]]

    return

# test find_sum
array = [2, 7, 11, 15]
target = 22

print(find_sum(array, target))