# Check whether the given character is Vowel or Consonant

character = input("Enter the character: ")

# if character == 'a' or character == 'e' or character == 'i' or character == 'o' == character == 'u':
if character in 'aeiouAEIOU':
    print("Character is a Vowel!")
else:
    print("Character is a Consonant!")

