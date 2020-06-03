from random import shuffle

# # Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space. (i.e. no creating a hashtable)
# Your runtime complexity should be less than O(n**2). (i.e. no double for loop)
# There is only one duplicate number in the array, but it could be repeated more than once.

# array = [1,2,3,5,2,2]

# sum(array)
# sum_of_1_to_n = max(array) * (max(array)+1) / 2


def find_duplicate(array):
    # My logical steps:
    # We find the biggest number in the array because finding the biggest number tells us many important things. 
    #   a) What numbers are used. If the duplicates didn't exist, each number from 1 to the biggest number would occur exactly once. So the number of unique numbers equals the biggest number.
    #   b) How many times the duplicate occurs. If n is the biggest number, and the length of the given array is n + k, then from fact 1 we know the duplicate occurs a total of k+1 times (it repeats k times)
    # Thus, if the number duplicated = d, the number of times the duplicate repeats = k (so k+1 total occurences), and the difference between the given array and the sum of 1 to n = s, then s = d * k. Thus d = s / k, i.e. the difference between the sum of the array and the sum of 1 to n, divided by the difference between the length of the array and the biggest number in the array.

    # we find the biggest number in the array
    highest_number = max(array)

    # we get the sum of the array with the duplicates
    array_sum = sum(array)

    # if the duplicates weren't here, the sum of the array would be n(n+1)/2 
    # In general, the sum of integers 1 to n is given by the formula ^^^
    sum_of_1_to_n = highest_number * (highest_number+1) /2

    # we get the difference between what the sum of 1 to n with the dupes is, and what the sum of 1 to n is without the dupes
    difference = array_sum - sum_of_1_to_n

    # we know the duplicate can occur more than twice, so we calculate how many times it occurs
    num_repeats = len(array) - highest_number

    # So, we know how many dupelicates there are. We know how much the difference is. we divide the difference by the number of repeats, and that gives us the duplicate number
    duplicate = difference/num_repeats

    # return as an integer, makes it return in the same type we got it in
    return int(duplicate)


# the same function as above, just in a one liner. Makes it clear that we only ever use O(1) space complexity
def find_duplicate_one_liner(array):
    return int((sum(array) - (max(array) * (max(array)+1) / 2)) / (len(array) - max(array)))


def cycle_search(array):
    tortoise = hare = array[0]

    # loop through cycle until the tortoise and hare meet
    while True:
        tortoise = array[tortoise]
        hare = array[array[hare]]
        if hare == tortoise:
            break
    
    # reset tortoise, slow down hare, continue until they meet at the duplicate
    tortoise = array[0]
    while tortoise != hare:
        tortoise = array[tortoise]
        hare = array[hare]
        if hare == tortoise:
            break
    
    return hare


array = [1,2,3,4,5,5,5,5,5,5]
duplicate = find_duplicate(array)
print(duplicate)
print(find_duplicate_one_liner(array))

array = [1,2,3,4,5,6,7,8,9,10,10,10]
duplicate = find_duplicate(array)
print(duplicate)
print(find_duplicate_one_liner(array))

array = [1,2,3,4,5,1]
duplicate = cycle_search(array)
print(duplicate)

array = [1,2,3,4,5,6,3]
shuffle(array)
duplicate = cycle_search(array)
print(duplicate)