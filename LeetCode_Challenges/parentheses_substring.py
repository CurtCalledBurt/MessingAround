string = "(()"
string = "(()()((((())))))))()(()()()"

def longest_parenth_substring(string):
    max_length = 0

    prev = ""
    length = 0
    for i in range(len(string)):
        if string[i] == ")":
            if prev == "(":
                length += 2
                if length > max_length:
                    max_length = length
            else:
                length = 0
        if string[i] == "(":
            if prev == "(":
                length = 0

        prev = string[i]

    return max_length

print(longest_parenth_substring(string))