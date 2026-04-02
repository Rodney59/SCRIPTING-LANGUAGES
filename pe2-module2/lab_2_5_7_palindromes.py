def is_palindrome(word):
    # Remove spaces and convert to lowercase
    word = word.replace(" ", "").lower()

    reversed_word = ""

    # Iterate through each character in the word
    for char in word:
        # Prepend the character to the reversed_word
        reversed_word = char + reversed_word

    # Check if the word is equal to its reversed version
    return word == reversed_word

# Example usage
user_word = input("Enter a word: ")
if is_palindrome(user_word):
    print(f"{user_word} is a palindrome.")
else:
    print(f"{user_word} is not a palindrome.")
