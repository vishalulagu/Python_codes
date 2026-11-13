# Check the two word is anagram?
# Anagrams conditions ;
#  - length of two words are equal.
#  - count of Each letter should match.
#  - Exactly match when both word's letters are alphabetically arranged.
# ---------------------------------------------------------------------------

word1 = "Care"
word2 = "Race"

def check_anagram(a, b):
    a = a.lower()
    b = b.lower()

    if len(a) != len(b):
        return f"{a} and {b} is not anagram."

    a = sorted(a)
    b = sorted(b)
    if a == b:
        return f"{a} and {b} is anagram."
    else:
        return f"{a} and {b} is not anagram."

print(check_anagram(word1, word2))