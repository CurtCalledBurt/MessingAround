# arr = [0,1,2]
# arr = [7,8,9,11,12]
# arr = [3,4,-1,1]
# arr = [ 0, 10, 2, -10, -20 , 1] 
arr = [2,-1,56,4]



# # #  ---- Naive Approach -----
# smallest_integer = 1
# smallest_int_found = False

# while not smallest_int_found:

#     for elem in arr:
#         if elem == smallest_integer:
#             smallest_integer += 1
#         else:
#             smallest_int_found = True
# print(smallest_integer)
# # # ----- End -----



# sends postive elements of the array to the front
print("array before neg/pos seperation: ", arr)
j = 0
for i in range(len(arr)): 
    if (arr[i] > 0): 
        arr[i], arr[j] = arr[j], arr[i] 
        j += 1 # increment count of positive integers  

num_non_postive_int = len(arr) - j

print("array after neg/pos seperation: ", arr)

num_postive_integers = j
print("Num pos ints: ", num_postive_integers)
print("Num neg ints: ", num_non_postive_int)

for i in range(num_postive_integers):
    if (abs(arr[i]) - 1 < num_postive_integers and arr[abs(arr[i]) - 1] > 0):
        arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

print("Print array with signs of int's flipped: ", arr)

smallest_missing_positve = 0
index = 0
while smallest_missing_positve == 0:
    if arr[index] >= 0:
        smallest_missing_positve = index + 1
    index += 1

print("Smallest missing positive int: ", smallest_missing_positve)
