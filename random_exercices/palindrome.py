def is_palindrome(word: str) -> bool:
    if not isinstance(word, str):
        raise TypeError(f"The argument must be a string, but you pass a {type(word)}")
    
    reverse_word = word[::-1]

    if reverse_word == word:
        return True
    else:
        return False

word = input("Enter a word: ")

try:
    if is_palindrome(word):
        print(f"{word.capitalize()} is a palindrome")
    else:
        print(f"{word.capitalize()} is not a palindrome") 
except TypeError as e:
    print(f"Error: {e}")

