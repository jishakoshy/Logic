list1 = [33, 44, 6, 7, 3, 44, 6, 33, 44]

# Lists to store elements and their counts
elements = []
counts = []

# Populate the elements and counts lists
for num in list1:
    if num in elements:
        index = elements.index(num)
        counts[index] += 1
    else:
        elements.append(num)
        counts.append(1)

# Find the most repeated value
max_count = 0
most_repeated_value = None

for i in range(len(elements)):
    if counts[i] > 1 and counts[i] > max_count:
        max_count = counts[i]
        most_repeated_value = elements[i]

if most_repeated_value is not None:
    print(f"The value repeated the most is: {most_repeated_value}, repeated {max_count} times.")
else:
    print("No duplicates found.")
