num1 = "123"
num2 = "987"


def get_digit_int(digit_str):
    if digit_str == "0":
        return 0
    elif digit_str == "1":
        return 1
    elif digit_str == "2":
        return 2
    elif digit_str == "3":
        return 3
    elif digit_str == "4":
        return 4
    elif digit_str == "5":
        return 5
    elif digit_str == "6":
        return 6
    elif digit_str == "7":
        return 7
    elif digit_str == "8":
        return 8
    elif digit_str == "9":
        return 9

def str_to_int(num_string):
    order_of_magnitude = 1
    num_int = 0
    for digit_string in num_string[::-1]:
        digit = get_digit_int(digit_string)
        num_int += digit * order_of_magnitude
        order_of_magnitude *= 10
    return num_int

def multiply_strings(num1, num2):
    return str_to_int(num1) * str_to_int(num2)

print(multiply_strings(num1=num1, num2=num2))
print(int(num1) * int(num2))
