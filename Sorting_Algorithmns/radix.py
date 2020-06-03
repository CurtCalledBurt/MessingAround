array = [170, 45, 75, 90, 802, 24, 2, 66]

def radix_sort(array):
    array = array.copy()
    num_loops = len(str(max(array)))

    place = 1
    for _ in range(num_loops):
        array.sort(key=lambda x: x / place % 10)
        place = place*10

    return array

array_sorted = radix_sort(array)
print(array_sorted)
print(array)