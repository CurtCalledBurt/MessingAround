nums = [1,8,6,2,5,4,3,5,7]

# take two numbers in the array, take the differences between the their indexes, multiply that by the smaller of the two, save that as the current maximum, and go to the next possible wall

used = set()
max_area = 0
for index_1 in range(len(nums)):
    used.add(index_1)
    for index_2 in range(len(nums)):
        if index_2 not in used:
            length = index_2 - index_1
            small_wall = min(nums[index_1], nums[index_2])
            if max_area < length * small_wall:
                max_area = length * small_wall

print(max_area)