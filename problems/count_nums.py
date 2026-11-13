# Count the each numbers in the list:

num_list = [7,2,0,0,7,0,6,9,7,2]
count = {}
for num in num_list:
    if num in count:
         #    Key    Value
        count[num] += 1
    else:
        count[num] = 1

print(count)
