def count_sort( arr, maximum=-1 ):
    print("\n\n Count Sort")
    # 1) creation of the count array
    # find maximum of the array
    for elem in arr:
        if elem > maximum:
            maximum = elem
    # create count array
    count_array = [0] * (maximum + 1)

    # 2) do the counting
    for i in range(len(arr)):
        count_array[arr[i]] += 1
    print( f" {count_array}")

    # 3) find the new indexes
    sum = 0
    sum_array = [0] * (maximum + 1)
    for i in range(len(count_array)):
        sum += count_array[i]
        sum_array[i] = sum
    print("\n", sum_array)

    # 4) put everything where it belongs
    
    return arr