"""
 Ask the user to enter a word or short sentence. Display the number of
characters, vowels (a, e, i, o, u), and spaces. Use a for loop to examine each character. Count uppercase
vowels as vowels too
"""
text = input("Enter a word or short sentence: ")

characters = len(text)
vowels = 0
spaces = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    if ch == " ":
        spaces += 1

print("Number of characters:", characters)
print("Number of vowels:", vowels)
print("Number of spaces:", spaces)