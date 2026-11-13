# Find the Duplicate Number in the List:

num_list = [7,2,0,0,7,0,6,9,7,2]
elements = []
duplicates = []

for num in num_list:
    if num in elements:
        duplicates.append(num)
    else:
        elements.append(num)
print(f"Elements: {elements}")
print(f"Duplicates: {duplicates}")
