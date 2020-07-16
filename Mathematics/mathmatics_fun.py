value_counts = {}

for i in range(1,7):
    for j in range(1,7):
        value = i + j + 2
        if value not in value_counts.keys():
            value_counts[value] = 1
        else:
            value_counts[value] += 1

print(value_counts)

print(10/36)