"""
A pangram is a sentence that contains every letter of the alphabet at least once.
"""


def checkPangram(phrase):
    letterset = set("abcdefghijklmnopqrstuvwxyz")
    phrase = {i.lower() for i in phrase if i.isalpha()}
    # This will take all the alphabets from the sentence and store in set in lower form.

    if phrase == letterset:
        return "This is an anagram!"
    else:
        return "It's not an anagram!"


print(checkPangram("The quick brown fox jumps over the lazy dog"))


