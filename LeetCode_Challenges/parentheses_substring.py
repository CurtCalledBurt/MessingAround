string = "(()"
string = "(()()((((())))))))()(()()()"

def longest_parenth_substring(string):
    max_length = 0

    prev = ""
    length = 0
    for i in range(len(string)):
        if string[i] == ")":
            if prev == "(": # complete pareth pair found, increase length of current substring by 2
                length += 2
                if length > max_length:
                    max_length = length
            else: # invalid pareth pair, start length over from 0
                length = 0
        if string[i] == "(":
            if prev == "(": # invalid pareth pair, starth length over from 0
                length = 0
            else: # potential continuation of valid substring,
                pass

        prev = string[i]

    return max_length

print(longest_parenth_substring(string))