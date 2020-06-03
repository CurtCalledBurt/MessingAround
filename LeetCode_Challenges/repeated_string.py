# counts how many 'a's there are in the first n letters of an infinitely repeated string s

def repeated_string(s, n):
    # count how many 'a's there are in the base string
    a_count = 0
    for letter in s:
        if letter == 'a':
            a_count += 1
    # alternate and probably faster way to count 'a'
    # a_count = s.count('a')
    
    # count how many times the string fits completely into n
    fits_completely = n // len(s)

    # how many of letters of 's' fit into the remaining amount of n
    remainder = n % len(s)

    # add and multiply up the results
    final_count = 0
    final_count += a_count * fits_completely

    # check if any 'a's are in the first remainder many of letters of s and add that to the count
    for i in range(remainder):
        if s[i] == 'a':
            final_count += 1
    # alternate and probably faster way to count 'a'
    # s[:remainder].count('a')
    
    return final_count


string = 'abcdefg'
n = 22
result = repeated_string(string, n)
print(f"In the first {n} characters of {string} repeated infinitely, 'a' occurs {result} time(s).")


string = 'abaa'
n = 48
result = repeated_string(string, n)
print(f"In the first {n} characters of {string} repeated infinitely, 'a' occurs {result} time(s).")
