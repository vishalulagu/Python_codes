# Reverse the Sentence

sentence = "I Love Python Language"
sentence_list = sentence.split()
reversed_list = []

# method 1
for word in sentence_list:
    reversed_list.insert(0, word)
reversed_sentence = " ".join(reversed_list)
print(reversed_sentence)

# method 2
reverse_sentence = " ".join(sentence.split()[::-1])
print(reverse_sentence)