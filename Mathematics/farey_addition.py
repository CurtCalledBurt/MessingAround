# Farey addition

# takes a decimal expansion, between 0 and 1, and finds the fraction closest to it

# initialize left fraction, initialize right fraction, 


# repeat starting here
# add fractions together, check which half the decimal is in

# replace old left/right fraction with new fraction.

# repeat until we have an acceptable level of error


decimal = 0.3333333333
error_bound = (1/10)**(12)
approximation = 1000000000000
approx_numerator = 0
approx_denominator = 1

left_numerator = 0
left_denominator = 1

right_numerator = 1
right_denominator = 1

while abs(approximation - decimal) > error_bound:
    new_numerator = left_numerator + right_numerator
    new_denominator = left_denominator + right_denominator

    # update left or right fraction
    if decimal < new_numerator/new_denominator:
        right_numerator = new_numerator
        right_denominator = new_denominator
    else:
        left_numerator = new_numerator
        left_denominator = new_denominator
    
    print("left fraction: ")
    print(left_numerator, left_denominator)
    print("right fraction: ")
    print(right_numerator, right_denominator)
    
    # update approximation with closer fraction
    if abs(approximation - left_numerator/left_denominator) < abs(approximation - right_numerator/right_denominator):
        approximation = left_numerator/left_denominator
        approx_numerator = left_numerator
        approx_denominator = left_numerator
    else:
        approximation = right_numerator/right_denominator
        approx_numerator = right_numerator
        approx_denominator = right_denominator
    
    # print(approx_numerator, approx_denominator)

print(approximation)
print(approx_numerator)
print(approx_denominator)
