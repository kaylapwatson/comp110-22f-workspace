"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730579974"

word: str = input("Enter a 5-character word:")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character:") 
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + word)

index0: str = word[0]
index1: str = word[1]
index2: str = word[2]
index3: str = word[3]
index4: str = word[4]

matching_char: int = 0

if character == word[0]:
    print(character + " found at index 0")
    matching_char = matching_char + 1
if character == word[1]:
    print(character + " found at index 1")
    matching_char = matching_char + 1
if character == word[2]:
    print(character + " found at index 2")
    matching_char = matching_char + 1
if character == word[3]:
    print(character + " found at index 3")
    matching_char = matching_char + 1
if character == word[4]:
    print(character + " found at index 4")
    matching_char = matching_char + 1

if matching_char == 0:
    print("No instances of " + character + " found in " + word)
if matching_char == 1:
    print("1 instances of " + character + " found in " + word)
if matching_char == 2:
    print("2 instances of " + character + " found in " + word)
if matching_char == 3:
    print("3 instances of " + character + " found in " + word)
if matching_char == 4:
    print("4 instances of " + character + " found in " + word)



