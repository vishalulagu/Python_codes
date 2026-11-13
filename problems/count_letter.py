# Count the each letters in the Word:

word = "Hello World"
count = {}
for letter in word:
    if letter in count:
        #       Key     Value
        count[letter] += 1
    else:
        count[letter] = 1
print(count)
