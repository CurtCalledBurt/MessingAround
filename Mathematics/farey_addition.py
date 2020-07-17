# Farey addition

# takes a decimal expansion, between 0 and 1, and finds the fraction closest to it

# initialize left fraction, initialize right fraction, 


# repeat starting here
# add fractions together, check which half the decimal is in

# replace old left/right fraction with new fraction.

# repeat as many times as we say to repeat the process


decimal = 0.3493827202
approximation = 1000000000000
approx_numerator = 0
approx_denominator = 1

left_numerator = 0
left_denominator = 1

right_numerator = 1
right_denominator = 1

iterations = 1_000_000

for _ in range(iterations):
    new_numerator = left_numerator + right_numerator
    new_denominator = left_denominator + right_denominator

    # update left or right fraction
    if decimal < new_numerator/new_denominator:
        right_numerator = new_numerator
        right_denominator = new_denominator
    else:
        left_numerator = new_numerator
        left_denominator = new_denominator

    if abs(approximation - left_numerator/left_denominator) < abs(approximation - right_numerator/right_denominator):
        approximation = left_numerator/left_denominator
        approx_numerator = left_numerator
        approx_denominator = left_numerator
    else:
        approximation = right_numerator/right_denominator
        approx_numerator = right_numerator
        approx_denominator = right_denominator


print(decimal)
print(approximation, '\n')
print(approx_numerator)
print('-----------')
print(approx_denominator)
