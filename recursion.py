# Print out each element of the following array on a separate line:
arr1 = ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]

# Print out each element of the following array on a separate line, but this time the input array can contain arrays nested to an arbitrarily deep level:
arr = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

def print_everything(arr):
    if type(arr) != list:
        print(arr)
    else:
        for elem in arr:
            print_everything(elem)

# print_everything(arr)
# print("\n\n")

def print_everything2(arr):
    if type(arr) == list:
        for elem in arr:
            print_everything2(elem)
    else:
        print(arr)

# print_everything2(arr)

def my_recursion(n):
    print(n)
    if n == 3:
        return
    my_recursion(n+1)
    my_recursion(n+1)

# my_recursion(1)



# Naive fibonacci
def get_nth_fibonacci(n):
    if n <= 1:
        return 1
    return get_nth_fibonacci(n - 1) + get_nth_fibonacci(n - 2)



# improved recursive fibonacci with recursion
def nth_fibonacci(n, cache={0: 1, 1: 1}):
    if n in cache:
        return cache[n]
    
    cache[n] = nth_fibonacci(n - 1) + nth_fibonacci(n - 2)
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

print('\n Fibonnacci \n')
print(nth_fibonacci(100))



def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    return n

# as of making this code, the max recursive steps we can take is 998, but that's a limit python
# imposes, not my computer. The calculation is nearly instantaneous in all cases the recursion limit 
# isn't reached
# print(f"\n Factorial \n {factorial(998)} \n")