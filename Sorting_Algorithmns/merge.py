def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    i = j = k = 0
    # merges elements in left and right arrays until one array is depleted
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1
    # finishes adding any elements to the merged array from the undepleted array
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1
    return merged_arr

def merge_sort( arr ):
    # base case is len(arr) < 2
    if len(arr) > 1:
        # get middle index
        mid_index = len(arr) // 2
        # divide array into two halves
        # in this case, by how python does splicing the pivot is in the right array
        # and recurse the function on the two split arrays to sort them individually
        left_arr = merge_sort(arr[:mid_index])
        right_arr = merge_sort(arr[mid_index:])

        # merge and sort the two sorted arrays together
        arr = merge(left_arr, 
                    right_arr)

    return arr

# functions to execute merge sort in place to conserve memory
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr