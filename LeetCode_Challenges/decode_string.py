# Examples:
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


# a function that defines and then calls a utility function that does the recursion. Stores a global variable for the recursive function to use
def decode_string(string):
    decoded_string = ""

    # function that does the decoding
    def decode_string_util(string):
        nonlocal decoded_string

        for i in range(len(string)):
            char = string[i]
            # get all letters before the first number onto the final string
            if char.isalpha():
                decoded_string += char
            # if digit, recurse on the stuff inside the brackets
            elif char.isdigit():
                n = int(char)
                bracket_count = 0
                start_bracket_index = 0
                end_bracket_index = 0
                #  sub_string is every char of the string except the digit
                sub_string = string[i+1:]
                for j in range(len(sub_string)):
                    letter = sub_string[j]
                    if letter == '[':
                        bracket_count += 1
                    elif letter == ']':
                        bracket_count -= 1
                        if bracket_count == 0:
                            end_bracket_index = j
                            break
                # repeat this sequence of letters n-1 many times
                for _ in range(n-1):
                    decode_string_util(sub_string[start_bracket_index+1: end_bracket_index])

    decode_string_util(string)
    return decoded_string


string = "ef3[a]2[bc]gh"
result = 'efaaabcbcgh'
decoded_str = decode_string(string)
print(decoded_str, "we made this")
print(result)
if decoded_str == result:
    print(True)
else:
    print(False)

string = "3[a2[c]]" 
result = "accaccacc"
decoded_str = decode_string(string)
print(decoded_str, "we made this")
print(result)
if decoded_str == result:
    print(True)
else:
    print(False)

string = "2[abc]3[cd]ef"
result = "abcabccdcdcdef"
decoded_str = decode_string(string)
print(decoded_str, "we made this")
print(result)
if decoded_str == result:
    print(True)
else:
    print(False)
    
string = "3[a2[c2[h]]de]fg" 
result = "achhchhdeachhchhdeachhchhdefg"
decoded_str = decode_string(string)
print(decoded_str, "we made this")
print(result)
if decoded_str == result:
    print(True)
else:
    print(False)
